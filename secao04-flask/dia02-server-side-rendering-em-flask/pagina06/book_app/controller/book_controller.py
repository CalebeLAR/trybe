from flask import Blueprint, render_template
from model.book_model import book

book_controller = Blueprint("book_controller", __name__)


@book_controller.route("/", methods=["GET"])
def index():
    return render_template(
        "book.html",
        year=book.year,
        title=book.title,
        author=book.author,
    )
