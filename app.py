from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = '6LfSZsgpAAAAAPCw8BEG2NoYDneC2b0RbLppBuDv'

@app.route('/')
def index():
    if 'registered' in session and session['registered']:
        return redirect(url_for('explore'))
    else:
        return redirect(url_for('register'))
    

@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Verify reCAPTCHA response
        recaptcha_response = request.form.get('g-recaptcha-response')
        if recaptcha_response:
            # Verify reCAPTCHA response with Google
            response = requests.post('https://www.google.com/recaptcha/api/siteverify', 
                                     data={'secret': '6LfSZsgpAAAAAPCw8BEG2NoYDneC2b0RbLppBuDv', 'response': recaptcha_response})
            data = response.json()
            if data['success']:
                # reCAPTCHA verification successful
                # Process registration here
                session['registered'] = True
                return redirect(url_for('explore'))
            else:
                # reCAPTCHA verification failed
                error_message = 'reCAPTCHA verification failed. Please try again.'
                return render_template('register.html', error_message=error_message)
        else:
            # No reCAPTCHA response provided
            error_message = 'reCAPTCHA verification failed. Please try again.'
            return render_template('register.html', error_message=error_message)
    return render_template('register.html')

@app.route('/chat_room')
def chat_room():
    if 'registered' in session and session['registered']:
        return render_template('chat_room.html')
    else:
        return redirect(url_for('register'))

@app.route('/create_room', methods=['GET', 'POST'])
def create_room():
    if request.method == 'POST':
        # Retrieve room details from form submission
        room_name = request.form.get('room_name')
        room_description = request.form.get('room_description')
        
        # Process the creation of the room (e.g., store details in database)
        # For demonstration, we'll just print the room details
        print(f"New Chat Room Created: Name - {room_name}, Description - {room_description}")
        
        # Redirect to the explore page after room creation
        return redirect(url_for('explore'))
    
    # Render the form for creating a new room
    return render_template('create_room.html')

if __name__ == '__main__':
    app.run(debug=True)
