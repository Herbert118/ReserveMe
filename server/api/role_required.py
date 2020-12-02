import settings
import jwt
import functools
from flask import request
import api.errors as error
import os

def permission(arg):

    def check_permissions(f):

        @functools.wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if auth is None and 'Authorization' in request.headers:
                try:
                    auth_type, token = request.headers['Authorization'].split(None, 1)
                    payload = jwt.decode(token,os.environ['SECRET_KEY'],algorithm='HS256')
                    if payload['sub'] < arg:
                        return error.NOT_ADMIN
                except ValueError:
                    return error.HEADER_NOT_FOUND
                except:
                    return error.INVALID_INPUT_422

            return f(*args, **kwargs)

        return decorated

    return check_permissions
