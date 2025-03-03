from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_mail import Message
from .forms import ContactForm
from . import mail  # Import the mail object from the package

# Create a Blueprint for views
bp = Blueprint('main', __name__)

###
# Routing for application.
###

@bp.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@bp.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@bp.route('/contact', methods=['GET', 'POST'])
@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Render contact page & handle form submission."""
    form = ContactForm()

    if form.validate_on_submit():  #  Part 4: Validate Form
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data  #  Part 5: Retrieve form data

        msg = Message(
            subject=subject,
            sender=(name, email),  
            recipients=["3ac0db265d-a42fe4@inbox.mailtrap.io"],  
            body=f"From: {name} <{email}>\n\n{message}"  
        )  

        try:
            with current_app.app_context():
                mail.send(msg)  
            flash("Your message has been sent successfully!", "success")
            return redirect(url_for("main.home"))
        except Exception as e:
            flash(f"Error sending email: {str(e)}", "danger")

    return render_template("contact.html", form=form)

@bp.route('/test-email')
def test_email():
    try:
        msg = Message(
            subject="Test Email",
            sender="noreply@yourdomain.com",  
            recipients=["your_mailtrap_inbox_email"], 
            body="This is a test email."
        )
        
        # Ensure that MailTrap is configured with the correct context
        with current_app.app_context():
            mail.send(msg)
        
        return "Test email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
    
###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@bp.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return current_app.send_static_file(file_dot_text)

@bp.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@bp.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404