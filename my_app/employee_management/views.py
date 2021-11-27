from my_app import app, db
from flask import render_template, request, flash, redirect, url_for
from my_app.employee_management.models import Employee


@app.route('/home')
def index():
    return render_template('index.html')
