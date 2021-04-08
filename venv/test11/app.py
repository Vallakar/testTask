import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres", password="987654321", host="localhost", port="5432", database="BaseA")
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres", password="987654321", host="localhost", port="5432", database="BaseA")

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # SQL-запрос для создания новой таблицы
    create_table_query = '''CREATE TABLE Cost
                              (ID serial PRIMARY KEY     NOT NULL,
                              name           TEXT    NOT NULL,                              
                              PRICE         REAL NOT NULL); '''
    cursor.execute(create_table_query)
    create_table_query = '''CREATE TABLE Products
                          (ID serial PRIMARY KEY     NOT NULL,
                          name           TEXT    NOT NULL,
                          status         TEXT    NOT NULL,
                          quantity      integer NOT NULL,
                          priceId       INTEGER REFERENCES     Cost (ID) ); '''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")