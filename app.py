
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'cicd_secret_key'  # Needed for flash messages

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if name and email and message:
            # Simulate sending an email by printing to console
            print(f"\n New Contact Message:\nFrom: {name} <{email}>\nMessage: {message}\n")
            flash(' Message sent successfully!', 'success')
            return redirect('/')
        else:
            flash(' Please fill in all fields.', 'error')

    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
