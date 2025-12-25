from flask import render_template, request, flash, redirect, session, url_for, abort, Blueprint
from .db import db
from .models import User, Feedback
import re

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html')

@main.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if not name or not email:
            flash('All fields are required!', 'error')

        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            flash('Invalid email address!', 'error')

        else :
            try:
                user = User(name=name, email=email)
                db.session.add(user)
                db.session.commit()
                flash('User created successfully!', 'success') 

                return redirect('/create_user')
            
            except Exception as e:
                db.session.rollback()
                flash('Error occurred: {}'.format(str(e)), 'error')

    return render_template('create_user.html')

@main.route('/login/<string:form_type>', methods=['GET', 'POST'])
def login(form_type):

    valid_form_types = ['view_feedback', 'feedback']
    if form_type not in valid_form_types:
        abort(404)

    if request.method == 'POST':
        email = request.form['email']

        if not email:
            flash('Email is required!', 'error')
        
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            flash('Invalid email address!', 'error')

        else:
            name = User.query.with_entities(User.name).filter_by(email=email).scalar()

            if name is None:
                flash('User not found!', 'error')
                return redirect(url_for('main.login', form_type=form_type))
            
            else:
                session['name'] = name
                session['email'] = email
                flash('Login successful!', 'success')

                if form_type == 'view_feedback':
                    return redirect(url_for('main.view_feedback'))
                
                else:
                    return redirect(url_for('main.feedback'))

    return render_template('login.html', form_type=form_type)

@main.route('/feedback' , methods=['GET', 'POST'])
def feedback():
    
    if request.method == 'POST':
        feedback = request.form['feedback']

        if not feedback:
            flash('Feedback is required!', 'error')
        
        else:
            try:
                user_id = User.query.with_entities(User.id).filter_by(email=session['email']).scalar()
                feedback = Feedback(feedback=feedback, user_id=user_id)
                db.session.add(feedback)
                db.session.commit()
                flash('Feedback submitted successfully!', 'success')
                return redirect('/feedback')
            
            except Exception as e:
                db.session.rollback()
                flash('Error occurred: {}'.format(str(e)), 'error')
    
    if 'name' not in session:
        flash('Please login to access feedback form!', 'error')
        return redirect(url_for('main.login', form_type='feedback'))
    
    else:
        return render_template('feedback.html', name = f"User : {session['name']}")
    



    
@main.route('/logout')
def logout():
    session.clear()
    flash('Logout successful!', 'success')
    return redirect('/')




@main.route('/view_feedback')
def view_feedback():
    if 'name' not in session:
        flash('Please login to view feedbacks!', 'error')
        return redirect(url_for('main.login', form_type='view_feedback'))
    
    
    else:
        feedbacks = Feedback.query.filter_by(user_id=User.query.with_entities(User.id).filter_by(email=session['email']).scalar()).all()
        return render_template('view_feedback.html', feedbacks=feedbacks, name = f"User : {session['name']}")

    

@main.route('/update_feedback/<int:feedback_id>', methods=['GET', 'POST'])
def update_feedback(feedback_id):

    if request.method == 'GET':

        if 'name' not in session:
            
            flash('Please login to access feedback form!', 'error')
            return redirect(url_for('main.login', form_type='view_feedback'))

        else:
            feedback = Feedback.query.filter_by(id=feedback_id).first()
            return render_template('update_feedback.html', feedback=feedback.feedback, name = f"User : {session['name']}", id = feedback_id)
    
    
    if request.method == 'POST':

        feedback_text = request.form['feedback']

        if not feedback_text:
            flash('Feedback is required!', 'error')

        else:

            try:

                feedback_record = Feedback.query.filter_by(id=feedback_id).first()
                feedback_record.feedback = feedback_text
                db.session.commit()
                flash('Feedback updated successfully!', 'success')
                return redirect(url_for('main.view_feedback'))
            
            except Exception as e:
                db.session.rollback()
                flash('Error occurred: {}'.format(str(e)), 'error')
                return redirect(url_for('main.view_feedback'))
            
@main.route('/delete_feedback/<int:feedback_id>', methods=['GET'])
def delete_feedback(feedback_id):
    if 'name' not in session:
        flash('Please login to delete feedbacks!', 'error')

    else:
        try:
            feedback = Feedback.query.filter_by(id=feedback_id).first()
            db.session.delete(feedback)
            db.session.commit()
            flash('Feedback deleted successfully!', 'success')
            return redirect(url_for('main.view_feedback'))
        
        except Exception as e:
            db.session.rollback()
            flash('Error occurred: {}'.format(str(e)), 'error')
            return redirect(url_for('main.view_feedback'))

                
@main.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    
    if request.method == 'POST':
        email = request.form['email']

        if not email:
            flash('Email is required!', 'error')
            return redirect(url_for('main.delete_user'))
        
        else:
            try:
                user = User.query.filter_by(email=email).first()
                db.session.delete(user)
                db.session.commit()
                flash('User deleted successfully!', 'success')
                return redirect(url_for('main.home'))
            
            except Exception as e:
                db.session.rollback()
                flash('Error occurred: {}'.format(str(e)), 'error')
                return redirect(url_for('main.delete_user'))
    
    return render_template('delete_user.html')