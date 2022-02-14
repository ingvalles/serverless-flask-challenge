from flask_sieve import Sieve
from flask_jwt_extended import JWTManager
from flask_caching import Cache

sieve = Sieve()
jwt = JWTManager()
cache = Cache()
