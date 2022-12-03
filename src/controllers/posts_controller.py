from flask import Flask,jsonify,request,make_response
from src.models.post import Post
from src.db.database import db
import logging # not necessary, for logging purpose only
from sqlalchemy import exc
from src.constants import http_status_codes

def get_all_posts():
    posts = Post.query.all()


    # Conver all posts to json and send back to do

    return "All posts"


def add_new_post():
    post_title  = request.json["title"]
    post_description = request.json["description"]
    post_postUrl  = request.json["postUrl"]

    new_post = Post(title=post_title,description=post_description,postUrl=post_postUrl)

    post_saved = save_post(new_post)


    
    if post_saved:
         # create response json object
        responseJson = jsonify({"status":"Created","Post":{"Post title: ":new_post.title,"Post description: ":new_post.description,"Post url: ":new_post.postUrl}})
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



# utils function
def save_post(post_object):
    print(post_object)
      # try add blog post to database
    try:
         db.session.add(post_object)
         db.session.commit()
         return True
    except exc.SQLAlchemyError as e:
        db.rollback()
        logging.error("Failed to Commit because of {error}. Doing Rollback".format(error=e))
        return False

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct