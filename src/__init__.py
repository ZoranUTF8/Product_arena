from flask import Flask
import os
from src.routes.auth import auth
from src.routes.posts import posts
from src.db.database import db
# Factory function for creating the app instance
def create_app(test_config=None):
   app = Flask(__name__, instance_relative_config=True)

   
   if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
        )
   else:
        app.config.from_mapping(test_config)
   
   
   db.init_app(app)

  
   app.register_blueprint(auth)
   app.register_blueprint(posts)



   return app


           