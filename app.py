# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded user credentials (replace with a database in production)
users = {
    'user': 'password',
    'vamshiburgula': 'vamshi@1609$',
    'chaithu_burgula': 'vb@1609',
}

@app.route('/')
def index():
    return render_template('index.html', error=None)

@app.route('/todolist')
def todolist():
    return render_template('todolist.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the provided username and password match
    if username in users and users[username] == password:
        return redirect(url_for('todolist'))
    else:
        return render_template('index.html', error='Invalid username or password')

if __name__ == '__main__':
    app.run(debug=True)
