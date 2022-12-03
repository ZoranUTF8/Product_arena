from flask import Flask,jsonify,request,make_response
from flask_login import login_user, logout_user
from src.constants import http_status_codes
from sqlalchemy import exc
from src.models.user import User
from src.db.database import db
from werkzeug.security import check_password_hash, generate_password_hash
import logging # not necessary, for logging purpose only



def register_user():
    email  = request.json["email"]
    password = request.json["password"]

    if User.query.filter_by(email=email).first():
        return jsonify({'error':"Email already in use. Pleas choose another one."})

    pwd_hash = generate_password_hash(password)

    new_user = User(email=email, passwordHash=pwd_hash)
    
      # try add blog post to database
    try:
         db.session.add(new_user)
         db.session.commit()
    except exc.SQLAlchemyError as e:
        db.rollback()
        logging.error("Failed to Commit because of {error}. Doing Rollback".format(error=e))


     # create response json object
    responseJson = jsonify({"status":"Created","User":{"user_email":new_user.email}})

    # make a response
    response = make_response(responseJson,http_status_codes.HTTP_201_CREATED)

    # add custom header
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
     
     #send back response
    return response

def login_user():
    email  = request.json["email"]
    password = request.json["password"]
    
    # Check if password is correct length
    if len(password) < 6:
        return jsonify({"error": "Invalid password"}).http_status_codes.HTTP_400_BAD_REQUEST

    # Check if email is registered in the database
    user = User.query.filter_by(email=email).first()

    

    return "login"

def logout_user():
    return "logout user"
