from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/projects')
def projects():
    return render_template('projects.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    flash('Form submitted succesfully', 'success')

    return redirect(url_for('views.contact'))
