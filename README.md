# Employee management with Flask framework

## Description

This repository contains an employee management project on a website. It was made in Python using the Flask framework. The database was created using MySQL Workbench.

## Creating a virtual environment

Open a terminal in your project directory and type the following command:

```bash
python -m venv venv
```
This will create a virtual environment named **venv**. To activate the virtual environment type the following command in your terminal:

```bash
"venv/scripts/activate.bat"
```

Next you have to install all required packages.


## Packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required packages, which are listed in the **requirements.txt** file. You can use the command below.

```bash
pip install -r requirements.txt
```

## Database

I used MySQL Workbench to store employee information. Create a new schema in the program. Then in the **my_app/\_\_init__.py** file you need to put some information about your database. In the following line of code, replace *user*, *password* and *schema* with the appropriate data.

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/schema'
```

It will provide a connection to your database. All tables will be created when you run the main **run.py** program. There are two tables named in lower case letters after model names such as *employee* and *user*.

## Launch

To run the application, use the **run.py** file found in the repository. You can use a terminal by typing the following command or run it from the IDE.

```bash
python run.py
```

This will start the local server. Then, in a web browser, enter the address given in the terminal like:

```
127.0.0.1:5000/
```

At this URL you will find the first web page of this application. This is the login page, so you must have an account to access the management system. You can create one by clicking on the registration link on the page. When you create a new account, details such as username and password will be stored in your database. You can now log into your account.

## Employee management

Once you have successfully logged in, you will have the option to add a new employee, update information about an existing employee or delete an existing one. You can also log out using the visible button on the *home* page.

I hope you enjoy using it :smiley:
