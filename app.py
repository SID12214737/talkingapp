from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['RECAPTCHA_PUBLIC_KEY'] = 'your_recaptcha_public_key_here'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'your_recaptcha_private_key_here'

# Generate a random user ID for each session
def generate_user_id():
    return str(uuid.uuid4())

# Form for user registration with CAPTCHA
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Register the user and generate a user ID
        session['user_id'] = generate_user_id()
        session['username'] = form.username.data
        return redirect(url_for('chat_room'))
    return render_template('register.html', form=form)

# Route for the chat room
@app.route('/', methods=['GET', 'POST'])
def chat_room():
    if 'user_id' not in session:
        return redirect(url_for('register'))
    
    # Handle form submission to update user alias
    if request.method == 'POST':
        user_alias = request.form.get('user_alias')
        if user_alias:
            session['user_alias'] = user_alias

    return render_template('chat_room.html', user_id=session['user_id'], user_alias=session.get('user_alias'))

if __name__ == '__main__':
    app.run(debug=True)
