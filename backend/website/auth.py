from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

hashed_password = 'c4b991b74c38acc0b4d0a145d7d0949c64af3abd3e8d29acd8cd7010ce0bb4a3'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')

        if check_password_hash(hashed_password, password):
            flash('Logged in successfully!', category='success')
            login_user({'username': username, 'password': hashed_password}, remember=True)
            return redirect(url_for('views.adddata'))
        else:
            flash('Incorrect password, try again.', category='error')
    else:
        flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

  
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))
