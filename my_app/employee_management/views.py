from my_app import app, db
from flask import render_template, request, flash, redirect, url_for
from my_app.employee_management.models import Employee


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        phone = request.form['phone']
        position = request.form['position']
        data = Employee(name, surname, email, phone, position)
        db.session.add(data)
        db.session.commit()
        flash("Employee added successfully!")

        return redirect(url_for('index'))

    else:
        return "test"
