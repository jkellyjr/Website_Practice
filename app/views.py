# app/views.py

from app import app
from flask import render_template, url_for, redirect
from .forms import ContactForm
from .emails import contact_email, return_email


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()

	if form.validate_on_submit() and form.human.data:
		name = form.name.data
		email = form.email.data
		msg = form.message.data
		contact_email(name, email, msg)
		if form.copy.data:
			return_email(name, email)
		return redirect(url_for('index'))

	return render_template('contact.html', form = form)
