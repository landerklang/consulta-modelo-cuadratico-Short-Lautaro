# import redis
# import json
# import sys
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# CACHE_HOST='0.0.0.0
# CACHE_PORT=5001
# MAX_CONSULTAS=5

# redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# app = Flask(__name__)
# CORS(app)

# app.route('/cache/get/<int:x>', methods=['GET'])
# def get_cache(x):
#     key = f'ecuacion:x:{x}"
#     cached = redis_client.get(key)
#     if cached:
#         print(f" Cache HIT para x={x}")
#         return jsonify({x': x, 'resultado': int(cached), 'origen': 'cache'})
#     else:
#         print(f" Cache MISS para x={x}")
#         return jsonify({x': x, 'resultado': None, 'origen': 'backend'})

# app.route('/cache/set/<int:x>/<int:y>, methods=['POST'])
# def set_cache(x, y):
#     key = f'ecuacion:x:{x}"
#     redis_client.push('consultas_recientes', x)
#     redis_client.set(key, y)
#     # Limitar a las ultimas MAX_CONSULTAS
#     if redis_client.len('consultas_recientes') > MAX_CONSULTAS:
#         oldest = redis_client.lpop('consultas_recientes')
#         if oldest:
#             redis_client.delete(f'ecuacion:x:{oldest}')
#             print(f" Cache purgeo: se elimino x={oldest}")
#     print(f" Cache SET para x={x}, y={y}")
#     return jsonify({status: "ok"})

# if __name__ == '__main__':
#     if len(sys.argv) > 1 and sys.argv[1] == 'clear':
#         redis_client.flushall()
#         print(" Cache limpia.do.")
#     else:
#         # Continuación en la segunda imagen