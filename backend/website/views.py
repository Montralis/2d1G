from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("/base/index.html")

@views.route('/add-data', methods=['GET', 'POST'])
@login_required
def addData():
    return render_template("/admin/add-data.html", user=current_user)
