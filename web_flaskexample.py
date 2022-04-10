# Import libraries

from flask import Flask, render_template

# Set default configuration variables
my_name = "Bill Dykema"
my_email = "bill@dykema.org"
my_contact = "https://www.linkedin.com/in/dykemabill"

# Create Flask app
my_app = Flask(__name__)

# Root landing page
@my_app.route('/')
def landing():
    if len(my_name) > 0 and len(my_email) > 0 and len(my_contact) > 0:
        return render_template('landing.html', name=my_name, email=my_email, contact=my_contact)
    else:
        return render_template('error.html')

# Run in debug mode if started from CLI (http://localhost:5000)
if __name__ == '__main__':
    my_app.run(debug=True)