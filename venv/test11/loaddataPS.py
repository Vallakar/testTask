import psycopg2
import random
import string
from psycopg2 import Error


try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres", password="987654321", host="localhost", port="5432", database="BaseA")
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    letters = string.ascii_letters
    # Вычищение базы от старых данных
    cursor.execute("truncate  Products CASCADE")
    cursor.execute("truncate  Cost CASCADE")
    cursor.execute("ALTER SEQUENCE Cost_ID_seq RESTART WITH 1")
    cursor.execute("ALTER SEQUENCE Products_ID_seq RESTART WITH 1")

    # заполнение случайными данными
    for i in range(20):
        result_name = ''.join(random.choice(letters) for j in range(8))
        result_price = random.randint(100, 100000)
        insert_query = """ INSERT INTO Cost (name, PRICE) VALUES (%s, %s) RETURNING id"""
        item_tuple = (result_name, result_price)
        cursor.execute(insert_query, item_tuple)
        id_of_new_row = cursor.fetchone()[0]
        list_status = ["enable", "disable"]
        result_status = random.choice(list_status)
        result_quantity = random.randint(0, 100)
        insert_query = """ INSERT INTO Products (name, status, quantity, priceId) VALUES (%s, %s, %s, %s)"""
        item_tuple = (result_name, result_status, result_quantity, id_of_new_row)
        cursor.execute(insert_query, item_tuple)
        connection.commit()

    # вывод заполненных данных для проверки корректности заполнения
    for i in range(20):
        cursor.execute("SELECT * from Cost WHERE ID = %s", (i+1,))
        record = cursor.fetchall()
        print("Результат postgres", record)
        cursor.execute("SELECT * from Products WHERE ID = %s", (i + 1,))
        record = cursor.fetchall()
        print("Результат postgres", record)


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

