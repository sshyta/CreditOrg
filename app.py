import sqlalchemy
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Item, Employee, Client  # Предполагая, что эти классы определены в models.py
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

app = Flask(__name__)

# Создание базового класса
Base = sqlalchemy.orm.declarative_base()

# Определение URI для базы данных
DATABASE_URI = 'postgresql://postgres:467912@localhost:5432/SSS'

# Создание двигателя (engine)
engine = create_engine(DATABASE_URI)

# Создание сессии (session) с использованием scoped_session
Session = scoped_session(sessionmaker(bind=engine))

@app.teardown_appcontext
def remove_session(exception=None):
    Session.remove()

# Маршрут для отображения главной страницы
@app.route('/')
def index():
    return render_template('index.html')

# Маршрут для отображения страницы добавления нового сотрудника
@app.route('/add_employee_page')
def add_employee_page():
    return render_template('add_employee.html')

# Маршрут для добавления нового сотрудника
@app.route('/add', methods=['POST'])
def add():
    employee_name = request.form['employee_name']
    employee_surname = request.form['employee_surname']
    job_title = request.form['job_title']
    salary = request.form['salary']
    start_date_str = request.form['start_date']

    # Преобразование строки с датой в объект datetime
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

    # Получение credit_check_id, если он есть в форме
    credit_check_id = request.form.get('credit_check_id')

    new_employee = Employee(
        employee_name=employee_name,
        employee_surname=employee_surname,
        job_title=job_title,
        salary=salary,
        start_date=start_date,
        credit_check_id=credit_check_id
    )
    session = Session()
    session.add(new_employee)
    session.commit()
    return redirect(url_for('index'))

# Маршрут для отображения списка сотрудников
@app.route('/view_employees')
def view_employees():
    session = Session()
    employees = session.query(Employee).all()
    return render_template('view_employees.html', employees=employees)

# Маршрут для отображения списка клиентов
@app.route('/view_clients')
def view_clients():
    session = Session()
    clients = session.query(Client).all()
    return render_template('view_clients.html', clients=clients)

if __name__ == '__main__':
    app.run(debug=True)