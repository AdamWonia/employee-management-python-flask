from my_app import app, db
from flask import render_template, request, flash, redirect, url_for
from my_app.employee_management.models import Employee, LoginForm, RegisterForm


@app.route('/home', methods=['GET'])
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        phone = request.form['number']
        position = request.form['position']
        employee = Employee(name, surname, email, phone, position)
        if employee:
            try:
                db.session.add(employee)
                db.session.commit()
                flash('Employee successfully added!')
                return redirect(url_for('index'))
            except Exception as e:
                return f"Something went wrong: {e}"
    else:
        return render_template('add.html')


@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id=None):
    employee = Employee.query.get_or_404(id)
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.surname = request.form['surname']
        employee.email = request.form['email']
        employee.phone = request.form['number']
        employee.position = request.form['position']
        try:
            db.session.commit()
            flash('Employee successfully updated!')
            return redirect(url_for('index'))
        except Exception as e:
            return f"Something went wrong: {e}"
    else:
        return render_template('update.html', employee=employee)


@app.route('/delete/<int:id>/')
def delete(id=None):
    employee = Employee.query.get_or_404(id)
    try:
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Something went wrong when updating the task: {e}"


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    return render_template('register.html', form=form)
