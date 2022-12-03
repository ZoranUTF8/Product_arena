from flask import Blueprint
from src.controllers import posts_controller


posts = Blueprint("posts",__name__,url_prefix="/api/v1/")

# Get all posts
@posts.get("/posts")
def get_posts():
    return posts_controller.get_all_posts()

# Add new posts
@posts.post("/posts")
def nes_post():
    return posts_controller.add_new_post()