from flask import Blueprint, render_template, request, flash


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@views.route('/addata', methods=['GET', 'POST'])
@login_required
def adddata():
    return render_template("addata.html", user=current_user)
