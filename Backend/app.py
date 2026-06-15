import redis
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# IMPORTANTE: Usar 10.0.2.2 (host) porque NAT aísla las VMs
# El puerto 5001 debe estar reenviado en VirtualBox a la VM Cache
cache_client = redis.Redis(
    host='127.0.0.1',      # IP del host (Windows) desde la VM
    port=6379,             # Puerto reenviado al cache
    decode_responses=True,
    socket_connect_timeout=2
)

@app.route('/calculator', methods=['POST'])
def calculator():
    data = request.get_json()
    x = data.get('x')
    
    # 1. Intentar obtener del cache
    try:
        cached_result = cache_client.get(f'eq:{x}')
        if cached_result is not None:
            print(f"Cache HIT para x={x}")
            return jsonify({
                "resultado": float(cached_result),
                "origen": "cache"
            })
        else:
            print(f"Cache MISS para x={x}")
    except Exception as e:
        print(f"Error conectando al cache: {e}")
    
    # 2. Calcular (no estaba en cache)
    resultado = 2 * (x ** 2) + 5 * x + 3
    print(f"Calculando: x={x} -> y={resultado}")
    
    # 3. Guardar en cache para futuras consultas
    try:
        cache_client.setex(f'eq:{x}', 3600, resultado)
        print(f"Guardado en cache: x={x} -> y={resultado}")
    except Exception as e:
        print(f"Error guardando en cache: {e}")
    
    return jsonify({
        "resultado": resultado,
        "origen": "backend"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)