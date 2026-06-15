### Cache
se importaro las dependencias para poder hacer funcionar el codigo 
**flask, redis, flask-cors**
luego se creo una archivo que se llama backend por error si fue cambiada esta parte tambien se eliminar y se colocar su  nuevo nombre, luego se le asigno una red nat.
se le asigno 2 reglas para el cache uno para que se pueda comunicar con las otras maquinas y otra para que poder comunicarse con el redis server

### Backend
se creo una variable de entorno para poder trabajar en el backend para hacer esto se escribio lo siguiente:**python3 -m venv env** una ves que esto se hiso le inicio el entorno con el siguiente comando **source venv/bin/activate** y de hay se instalaron las dependencia que desesita el codigo **pip install flask flask-cors redis requests** y por ultimo para iniciar el backend debe escribir lo siguiente **python3 backend.py**

*nota para instalar el python3 si no lo tienes tienes que escribir los siguiente sudo apt install python3 -y*

### Frontend

el proceso del frontend es igual pero debe de iniciar de esta forma ![alt text](image.png)