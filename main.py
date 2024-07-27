from flask import Flask, render_template
from logic.auth import auth_bp
from logic.password_manager import password_manager_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a strong, secret key

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(password_manager_bp, url_prefix='/password_manager')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user_home')
def user_home():
    return redirect(url_for('password_manager.user_home'))

if __name__ == '__main__':
    app.run(debug=True)
