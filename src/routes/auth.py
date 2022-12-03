from flask import Blueprint
from src.controllers import auth_controller

auth = Blueprint("auth",__name__,url_prefix="/api/v1/auth")

@auth.post("/register")
def register():
   return auth_controller.register_user()
