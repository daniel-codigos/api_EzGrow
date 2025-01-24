import jwt, datetime
from rest_framework import exceptions
from dotenv import load_dotenv
import os

# Cargar el archivo .env
ruta = os.getcwd()
print(ruta)
load_dotenv(ruta+"/cred.env")
# Acceder a las credenciales
SECRET_KEY = os.getenv("secret")


def create_access_token(id,email):
    return jwt.encode({
        'user_id': id,
        'email':email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=55),
        'iat': datetime.datetime.utcnow()
    }, SECRET_KEY,algorithm='HS256')


def decode_access_token(token):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms='HS256')

        return payload['user_id'],payload['email']
    except:
        raise exceptions.AuthenticationFailed('Desautentificado!! jiji')

def create_refresh_token(id,email):
    return jwt.encode({
        'user_id': id,
        'email':email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }, SECRET_KEY,algorithm='HS256')


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')

        return payload['user_id'],payload['email']
    except:
        raise exceptions.AuthenticationFailed('Desautentificado!! jeje')