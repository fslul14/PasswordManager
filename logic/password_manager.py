from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import json
import os
import re
import random
import string

password_manager_bp = Blueprint('password_manager', __name__)

# Define the path for the passwords.json and weakpass.txt files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASSWORDS_FILE = os.path.join(BASE_DIR, 'passwords.json')
WEAKPASS_FILE = os.path.join(BASE_DIR, 'weakpass.txt')

def ensure_passwords_file_exists():
    """Create an empty passwords.json file if it does not exist."""
    if not os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'w') as file:
            json.dump({}, file)

def load_weak_passwords():
    """Load weak passwords from weakpass.txt into a set."""
    if not os.path.exists(WEAKPASS_FILE):
        return set()
    with open(WEAKPASS_FILE, 'r') as file:
        return set(line.strip() for line in file)

def check_password_strength(password):
    """Check if the password meets the required strength criteria."""
    if len(password) < 8 or len(password) > 16:
        return 'Weak'
    if not re.search(r'[A-Z]', password):  # Check for uppercase letter
        return 'Weak'
    if not re.search(r'[a-z]', password):  # Check for lowercase letter
        return 'Weak'
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Check for special character
        return 'Weak'
    return 'Strong'

def generate_password():
    """Generate a random password that meets the strength criteria."""
    while True:
        length = random.randint(8, 16)
        password = (
            ''.join(random.choices(string.ascii_uppercase, k=1)) +
            ''.join(random.choices(string.ascii_lowercase, k=1)) +
            ''.join(random.choices(string.digits + string.punctuation, k=length - 2))
        )
        password = ''.join(random.sample(password, len(password)))
        if check_password_strength(password) == 'Strong':
            return password

@password_manager_bp.route('/add_password', methods=['POST'])
def add_password():
    ensure_passwords_file_exists()  # Ensure the passwords file exists
    website = request.form['website']
    username = request.form['username']
    password = request.form['password']
    if not website or not username or not password:
        return "Please fill in all fields."
    with open(PASSWORDS_FILE, 'r') as file:
        passwords = json.load(file)
    passwords[website] = {'username': username, 'password': password}
    with open(PASSWORDS_FILE, 'w') as file:
        json.dump(passwords, file)
    return redirect(url_for('password_manager.user_home'))

@password_manager_bp.route('/user_home')
def user_home():
    ensure_passwords_file_exists()  # Ensure the passwords file exists
    weak_passwords = load_weak_passwords()  # Load weak passwords
    with open(PASSWORDS_FILE, 'r') as file:
        passwords = json.load(file)
    
    # Add strength information to each password
    for website, creds in passwords.items():
        password = creds['password']
        if password in weak_passwords:
            creds['strength'] = 'Weak'
        else:
            creds['strength'] = check_password_strength(password)
    
    return render_template('user_home.html', passwords=passwords)

@password_manager_bp.route('/edit_password', methods=['POST'])
def edit_password():
    ensure_passwords_file_exists()  # Ensure the passwords file exists
    website = request.form['website']
    username = request.form['username']
    password = request.form['password']
    if not username or not password:
        return "Please fill in all fields."
    with open(PASSWORDS_FILE, 'r') as file:
        passwords = json.load(file)
    if website in passwords:
        passwords[website] = {'username': username, 'password': password}
        with open(PASSWORDS_FILE, 'w') as file:
            json.dump(passwords, file)
    return redirect(url_for('password_manager.user_home'))

@password_manager_bp.route('/delete_password/<string:website>', methods=['POST'])
def delete_password(website):
    ensure_passwords_file_exists()  # Ensure the passwords file exists
    with open(PASSWORDS_FILE, 'r') as file:
        passwords = json.load(file)
    if website in passwords:
        del passwords[website]
        with open(PASSWORDS_FILE, 'w') as file:
            json.dump(passwords, file)
    return redirect(url_for('password_manager.user_home'))

@password_manager_bp.route('/suggest_password', methods=['GET'])
def suggest_password():
    """Route to suggest a new strong password."""
    password = generate_password()
    return jsonify({'password': password})
