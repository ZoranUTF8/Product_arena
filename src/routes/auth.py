from flask import Blueprint,request
from src.controllers import auth_controller

auth = Blueprint("auth",__name__,url_prefix="/api/v1/auth")



'''
Register a user
'''
@auth.post("/register")
def logout():
   return auth_controller.register_user()


'''
Login a user with the provided email and password
'''
@auth.post("/login")
def login():
   return auth_controller.login_user()

'''
Logout a user
'''
# @auth.post("/logout")
# def logout():
#    return auth_controller.logout_user()

