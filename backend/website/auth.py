import os
from flask import Blueprint, render_template, request , redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user, UserMixin


auth = Blueprint('auth', __name__)


# Singleton user design for login
class User(UserMixin):
    id = 1

    def __init__(self, user_password):
        pass
        self.hashed_password = generate_password_hash(user_password)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        user = User(os.getenv('USER_PASSWORD'))

        if check_password_hash(user.hashed_password, password):
            login_user(user)
            flash('You are now logged in.')
            return redirect(url_for('views.addData'))
        else:
            flash('Incorrect password, please try again.', category='error')

    return render_template("/admin/login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))
