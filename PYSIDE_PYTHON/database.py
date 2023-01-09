import PySide6.QtSql

# utwórz obiekt QSqlDatabase
db = PySide6.QtSql.QSqlDatabase.addDatabase("QSQLITE")

# ustaw nazwę bazy danych
db.setDatabaseName("mydatabase.db")

# otwórz połączenie z bazą danych
if not db.open():
    print("Nie udało się otworzyć połączenia z bazą danych")

# utwórz obiekt QSqlQuery i wykonaj polecenie DROP TABLE (jeśli tabela istnieje)
query = PySide6.QtSql.QSqlQuery()
query.exec_("DROP TABLE IF EXISTS users")

# utwórz obiekt QSqlQuery i wykonaj polecenie CREATE TABLE
query = PySide6.QtSql.QSqlQuery()
query.exec_("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)")

# utwórz obiekt QSqlQuery i wykonaj zapytanie INSERT
query = PySide6.QtSql.QSqlQuery()
query.exec_("INSERT INTO users (id, username) VALUES (1, 'johndoe')")
query.exec_("INSERT INTO users (id, username) VALUES (2, 'janedoe')")
query.exec_("INSERT INTO users (id, username) VALUES (3, 'janedoee')")

# utwórz obiekt QSqlQuery i wykonaj zapytanie SELECT
query = PySide6.QtSql.QSqlQuery()
query.exec_("SELECT * FROM users")

# pobierz wyniki zapytania
while query.next():
    user_id = query.value(0)
    username = query.value(1)
    print(f"ID: {user_id}, nazwa użytkownika: {username}")

# zamknij połączenie z bazą danych
db.close()

