from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = '6LfSZsgpAAAAAPCw8BEG2NoYDneC2b0RbLppBuDv'

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
                return redirect(url_for('chat_room'))
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


if __name__ == '__main__':
    app.run(debug=True)
