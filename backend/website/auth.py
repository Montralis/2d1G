import os
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user, UserMixin


auth = Blueprint('auth', __name__)

# Singelton User Design for Login
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
            print('Password is correct, user is logged in')
            return redirect(url_for('views.adddata'))
        else:
            print('Incorrect password, try again.')

    return render_template("/admin/login.html", user=current_user)

  
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))
