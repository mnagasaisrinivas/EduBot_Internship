from flask import render_template, request, redirect, flash
import re
from app.db import insert_feedback, get_all_feedback

def configure_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/feedback')
    def feedback_form():
        return render_template('feedback_form.html')

    @app.route('/submit_feedback', methods=['POST'])
    def submit_feedback():
        name = request.form.get('name')
        email = request.form.get('email')
        feedback = request.form.get('feedback')

        if not name or not email or not feedback:
            flash('All fields are required!', 'error')
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            flash('Invalid email address!', 'error')
        else:
            insert_feedback(name, email, feedback)
            flash('Feedback submitted successfully!', 'success')
            return redirect('/feedback')

        return redirect('/feedback')

    @app.route('/view_feedback')
    def view_feedback():
        feedback_list = get_all_feedback()
        return render_template('feedback_list.html', feedback=feedback_list)
