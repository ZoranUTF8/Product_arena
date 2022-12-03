from flask import Blueprint
from src.controllers import lessons_controller


lessons = Blueprint("lessons",__name__,url_prefix="/api/v1/")


@lessons.get("/lessons")
def get_lessons():
    return lessons_controller.get_all_lessons()
