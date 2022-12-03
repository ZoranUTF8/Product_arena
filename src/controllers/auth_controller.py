from flask import Flask,jsonify,request,make_response
from src.constants import http_status_codes
from sqlalchemy import exc
from src.models.user import User
from src.db.database import db
from werkzeug.security import check_password_hash, generate_password_hash
import logging # not necessary, for logging purpose only


# Register a new user
def register_user():
    email  = request.json["email"]
    password = request.json["password"]

    email_in_use = check_if_email_is_valid(email)

    if email_in_use:
        return jsonify({'error':"Email already in use. Pleas choose another one."})

    # Generate password hash
    pwd_hash = generate_password_hash(password)

    # Create new user
    new_user = User(email=email, passwordHash=pwd_hash)
    
    # Add user to database
    user_saved = save_user(new_user)

    if user_saved:
         # create response json object
        responseJson = jsonify({"status":"Created","User":{"user_email":new_user.email}})
         # make a response
        response = make_response(responseJson,http_status_codes.HTTP_201_CREATED)
        # add custom header
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        #send back response
        return response
    
    else:
        responseJson = jsonify({"status":"Error",})
         # make a response
        response = make_response(responseJson,http_status_codes.HTTP_500_INTERNAL_SERVER_ERROR)
        # add custom header
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        #send back response
        return response

# Login request
def login_user():
    email  = request.json["email"]
    password = request.json["password"]

    # Check if email is registered in the database
    user = User.query.filter_by(email=email).first()

    if user:
        password_match = check_password_hash(user.passwordHash,password)

        if password_match:
         # create response json object
            responseJson = jsonify({"status":"Success","User":{"user_email":user.email}})
         # make a response
            response = make_response(responseJson,http_status_codes.HTTP_200_OK)
        # add custom header
            response.headers['Content-Type'] = 'application/json; charset=utf-8'
        #send back response
            return response
        else:
            responseJson = jsonify({"status":"Error","message":"Pogrešan email ili password"})
         # make a response
            response = make_response(responseJson,http_status_codes.HTTP_400_BAD_REQUEST)
        # add custom header
            response.headers['Content-Type'] = 'application/json; charset=utf-8'
        #send back response
            return response

# Logout request to do
def logout_user():

    return "logout user"


# utils functions

def check_if_email_is_valid(email):
    if User.query.filter_by(email=email).first():
        return True

def save_user(user_object):
      # try add blog post to database
    try:
         db.session.add(user_object)
         db.session.commit()
         return True
    except exc.SQLAlchemyError as e:
        db.rollback()
        logging.error("Failed to Commit because of {error}. Doing Rollback".format(error=e))
        return False

