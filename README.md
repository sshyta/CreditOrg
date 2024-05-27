# CreditOrg
<img width="647" alt="Снимок экрана 2024-05-27 в 10 37 43" src="https://github.com/sshyta/CreditOrg/assets/86688897/8774abcf-e029-45a0-a27b-7818ffdbdc41">
Веб-приложение, разработанное с использованием Flask и SQLAlchemy, представляет собой систему управления данными для организации, занимающейся кредитами.

<img width="592" alt="Снимок экрана 2024-05-27 в 10 39 43" src="https://github.com/sshyta/CreditOrg/assets/86688897/5423d94a-9d5c-4cb6-929d-45efad94cd32">
##Определение URI для базы данных:
Создали строку подключения к базе данных PostgreSQL, используя информацию о имени пользователя, пароле, хосте и названии базы данных:
DATABASE_URI = 'postgresql://username:467912@hostname/SSS'
Здесь username - имя пользователя PostgreSQL, 467912 пароль, hostname - хост (обычно localhost для локальной базы данных), SSS - название базы данных.

##Создание двигателя (engine):
Создали объект двигателя с помощью функции create_engine(), передав ей строку подключения:
engine = create_engine(DATABASE_URI)
Этот двигатель представляет собой интерфейс к базе данных.

##Создание сессии (session):
Использовали sessionmaker() для создания класса сеанса (session), связанного с нашим двигателем:

Session = sessionmaker(bind=engine)
session = Session()
Этот объект сессии позволяет нам выполнять операции с базой данных, такие как добавление, изменение и извлечение данных.

##Определение структуры таблиц:
Определяем структуру каждой таблицы в базе данных, создавая классы для каждой из них и наследуя их от Base, который является экземпляром declarative_base()
После создания объекта сессии мы можем использовать его для выполнения запросов к базе данных, таких как добавление новых записей или извлечение данных.

