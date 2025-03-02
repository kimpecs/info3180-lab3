from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_mail import Message
from .forms import ContactForm
from . import mail 

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
def contact():
    """Render the website's contact page and handle form submission."""
    form = ContactForm()  # Create an instance of the ContactForm

    if form.validate_on_submit():
        # Construct the email message
        msg = Message(
            subject=form.subject.data,
            sender=(form.name.data, form.email.data),  # Use form sender data
            recipients=["recipient@example.com"]  # Replace with actual recipient email
        )
        msg.body = f"""
        From: {form.name.data} <{form.email.data}>
        Subject: {form.subject.data}

        Message:
        {form.message.data}
        """  # Email body with user input
        try:
            mail.send(msg)  # Send the email
            flash("Your message has been sent successfully!", "success")
            return redirect(url_for("main.home")) 
        except Exception as e:
            flash(f"An error occurred while sending the email: {str(e)}", "danger")

    return render_template("contact.html", form=form)

@bp.route('/test-email')
def test_email():
    try:
        msg = Message(
            subject="Test Email",
            sender=current_app.config['MAIL_DEFAULT_SENDER'],
            recipients=["recipient@example.com"]
        )
        msg.body = "This is a test email."
        mail.send(msg)
        return "Email sent successfully!"
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