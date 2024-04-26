from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Verify reCAPTCHA token
        token = request.form.get('g-recaptcha-response')
        if token:
            response = requests.post('https://www.google.com/recaptcha/api/siteverify', 
                                     data={'secret': 'your_secret_key_here', 'response': token})
            data = response.json()
            if data['success'] and data['score'] >= 0.5:
                # reCAPTCHA verification successful
                # Process registration here
                session['registered'] = True
                return redirect(url_for('chat_room'))
            else:
                # reCAPTCHA verification failed
                error_message = 'reCAPTCHA verification failed. Please try again.'
                return render_template('register.html', error_message=error_message)
        else:
            # No reCAPTCHA token found
            error_message = 'reCAPTCHA token missing. Please try again.'
            return render_template('register.html', error_message=error_message)
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
