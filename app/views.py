from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_mail import Message  # Import Message
from . import mail  # Import the mail object from the app package
from .config import Config
from .forms import ContactForm

# Create a Blueprint
bp = Blueprint('main', __name__)

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
    """Render and process the contact form."""
    form = ContactForm()
    if form.validate_on_submit():
        # Get form data
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        # Create and send the email
        msg = Message(
            subject=subject,
            sender=('Your Name', Config.MAIL_DEFAULT_SENDER),
            recipients=[email]
        )
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)  # Use the mail object imported from app

        # Flash a success message and redirect to the home page
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('main.home'))

    # Flash form errors if validation fails
    flash_errors(form)
    return render_template('contact.html', form=form)

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')