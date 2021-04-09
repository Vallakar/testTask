import psycopg2
from psycopg2 import Error
import mysql.connector

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres", password="987654321", host="localhost", port="5432", database="BaseA")
    cursor = connection.cursor()
    # SQL-запрос для создания новой таблицы
    create_table_query = '''CREATE TABLE Cost
                              (ID serial PRIMARY KEY     NOT NULL,
                              name           TEXT    NOT NULL,                              
                              PRICE         INT NOT NULL); '''
    cursor.execute(create_table_query)
    create_table_query = '''CREATE TABLE Products
                          (ID serial PRIMARY KEY     NOT NULL,
                          name           TEXT    NOT NULL,
                          status         TEXT    NOT NULL,
                          quantity      integer NOT NULL,
                          priceId       INTEGER REFERENCES     Cost (ID) ); '''
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
