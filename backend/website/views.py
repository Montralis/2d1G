from flask import Blueprint, render_template, request, flash


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

