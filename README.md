# testTask
Создал docker-compose с поднятием 2 контейнеров с mysql и postgres c подключениям к ним volume для хранения данных

Создал app.py в котором создается база в postgres

Создал loaddataPS.py где заполняется база postgres случайными данными и для проверки выводит их в строку
Чтобы каждый раз не убивать volume для чистки базы, то перед заполнением база чиститься и все счетчики ID сбрасываются

Встрял на подключении к mysql, при попытке выдает ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
то же при подключении отдельно созданного пользователя

Попробовал подключаться docker exec -it testtask_dbmysql_1  mysql -uroot -p
Выдает тоже

docker exec -it testtask_dbmysql_1  mysql -uroot -p
Enter password:
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)

пока есть только подозрения, что localhost при авторизации отрабатывает как root localhost системы где запускается скрип и не соотвествет пользователю root@localhost в контейнере
