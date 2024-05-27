import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Определение базового класса
Base = sqlalchemy.orm.declarative_base()

# Определение структуры таблицы
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

# Замените значения на ваши данные
DATABASE_URI = 'postgresql://postgres:467912@localhost:5432/SSS'

# Создание двигателя (engine)
engine = create_engine(DATABASE_URI)

# Создание сессии (session)
Session = sessionmaker(bind=engine)
session = Session()

# Определение классов таблиц
class CreditOrg(Base):
    __tablename__ = 'credit_org'
    credit_org_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    credit_operation_id = Column(Integer)
    client_id = Column(Integer)
    credit_check_id = Column(Integer)
    debtor_id = Column(Integer)
    credit_org_name = Column(String)
    credit_org_address = Column(String)
    city = Column(String)
    phone_number = Column(String)

class CreditOperation(Base):
    __tablename__ = 'credit_operation'
    credit_operation_id = Column(Integer, primary_key=True)
    credit_sum = Column(Float)
    interest_rate = Column(Float)
    credit_term = Column(Integer)
    credit_operation = Column(String)
    date_opening = Column(Date)
    status = Column(String)

class CreditCheck(Base):
    __tablename__ = 'credit_check'
    credit_check_id = Column(Integer, primary_key=True)
    interest_rate = Column(Float)
    credit_term = Column(Integer)
    credit_operation = Column(String)
    date_opening = Column(Date)
    status = Column(String)
    amount_of_credit = Column(Float)

class Administrator(Base):
    __tablename__ = 'administrator'
    administrator_id = Column(Integer, primary_key=True)
    administrator_name = Column(String)
    administrator_surname = Column(String)
    job_title = Column(String)
    salary = Column(Float)
    start_date = Column(Date)

class Employee(Base):
    __tablename__ = 'employee'
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    credit_check_id = Column(Integer, nullable=True)
    employee_name = Column(String)
    employee_surname = Column(String)
    job_title = Column(String)
    salary = Column(Integer)
    start_date = Column(Date)

class Client(Base):
    __tablename__ = 'client'
    client_id = Column(Integer, primary_key=True)
    client_name = Column(String)
    client_surname = Column(String)
    amount_of_debt = Column(Integer)
    date_of_delay = Column(Date)
    phone_number = Column(String)
    status = Column(String)

# Создание таблиц в базе данных
Base.metadata.create_all(engine)

# Функция для добавления нового объекта CreditOrg
def add_credit_org(employee_id, credit_operation_id, client_id, credit_check_id, debtor_id, credit_org_name, credit_org_address, city, phone_number):
    new_credit_org = CreditOrg(employee_id=employee_id, credit_operation_id=credit_operation_id, client_id=client_id, credit_check_id=credit_check_id, debtor_id=debtor_id,
                               credit_org_name=credit_org_name, credit_org_address=credit_org_address, city=city, phone_number=phone_number)
    session.add(new_credit_org)
    session.commit()

# Функция для добавления нового объекта CreditOperation
def add_credit_operation(credit_sum, interest_rate, credit_term, credit_operation, date_opening, status):
    new_credit_operation = CreditOperation(credit_sum=credit_sum, interest_rate=interest_rate, credit_term=credit_term, credit_operation=credit_operation,
                                           date_opening=date_opening, status=status)
    session.add(new_credit_operation)
    session.commit()

# Функция для добавления нового объекта CreditCheck
def add_credit_check(interest_rate, credit_term, credit_operation, date_opening, status, amount_of_credit):
    new_credit_check = CreditCheck(interest_rate=interest_rate, credit_term=credit_term, credit_operation=credit_operation,
                                   date_opening=date_opening, status=status, amount_of_credit=amount_of_credit)
    session.add(new_credit_check)
    session.commit()

# Функция для добавления нового объекта Administrator
def add_administrator(administrator_name, administrator_surname, job_title, salary, start_date):
    new_administrator = Administrator(administrator_name=administrator_name, administrator_surname=administrator_surname, job_title=job_title,
                                      salary=salary, start_date=start_date)
    session.add(new_administrator)
    session.commit()

# Функция для добавления нового объекта Employee
def add_employee(credit_check_id, employee_name, employee_surname, job_title, salary, start_date):
    new_employee = Employee(credit_check_id=credit_check_id, employee_name=employee_name, employee_surname=employee_surname, job_title=job_title,
                            salary=salary, start_date=start_date)
    session.add(new_employee)
    session.commit()

# Функция для добавления нового объекта Client
def add_client(client_name, client_surname, amount_of_debt, date_of_delay, phone_number, status):
    new_client = Client(client_name=client_name, client_surname=client_surname, amount_of_debt=amount_of_debt,
                        date_of_delay=date_of_delay, phone_number=phone_number, status=status)
    session.add(new_client)
    session.commit()


