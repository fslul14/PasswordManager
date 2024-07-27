from flask import Blueprint, render_template, request, redirect, url_for, session
import json
import bcrypt
import os

auth_bp = Blueprint('auth', __name__)

# Define the path for the users.json file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, 'users.json')

def ensure_users_file_exists():
    """Create an empty users.json file if it does not exist."""
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as file:
            json.dump({}, file)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    ensure_users_file_exists()  # Ensure the users file exists
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            return "Please fill in all fields."
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # Save user to users.json
        with open(USERS_FILE, 'r') as file:
            users = json.load(file)
        if username in users:
            return "Username already exists. Please choose a different one."
        users[username] = hashed_password.decode('utf-8')
        with open(USERS_FILE, 'w') as file:
            json.dump(users, file)
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    ensure_users_file_exists()  # Ensure the users file exists
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open(USERS_FILE, 'r') as file:
            users = json.load(file)
        hashed_password = users.get(username)
        if hashed_password and bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            session['username'] = username
            return redirect(url_for('password_manager.user_home'))
        return "Invalid credentials. Please try again."
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth.login'))
