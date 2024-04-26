from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the login page
@app.route('/login')
def login():
    return render_template('login.html')

# Route for the registration page
@app.route('/register')
def register():
    return render_template('register.html')

# Route for a sample chat room page
@app.route('/chat-room')
def chat_room():
    return render_template('chat_room.html')

if __name__ == '__main__':
    app.run(debug=True)
