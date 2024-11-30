import pymysql
from decouple import config

DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

users = [
    ("user1", "password11", "codigo11@gmai.com"),
    ("user2", "password12", "codigo12@gmai.com"),
    ("user3", "password13", "gaga@gmai.com"),
    ("user4", "password14", "codigo3@gmai.com"),
]

if __name__ == '__main__':
    try:
        connect = pymysql.Connect(
            host='localhost', port=3306, user='root', passwd='root', db='pythondb'
        )

        with connect.cursor() as cursor:
            # Crear tabla y datos iniciales
            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)

            query = "INSERT INTO users(username,password,email) VALUES(%s,%s,%s)"
            for user in users:
                cursor.execute(query, user)
            connect.commit()

            # Consultar datos
            query = "SELECT id, username, email FROM users ORDER BY id ASC"
            cursor.execute(query)

            print("Datos antes de la actualización:")
            for user in cursor.fetchall():
                print(user)

            # Actualizar registro
            update_query = "UPDATE users SET username=%s WHERE id=%s"
            update_values = ("cambio de username", 1)
            cursor.execute(update_query, update_values)
            connect.commit()

            # Consultar datos nuevamente para verificar la actualización
            cursor.execute(query)
            print("\nDatos después de la actualización:")
            for user in cursor.fetchall():
                print(user)

            #eliminar datos 
            query = "DELETE FROM users WHERE id=%s"
            cursor.execute(query,(3,))
            connect.commit()
    

    except pymysql.err.OperationalError as err:
        print("No fue posible completar la operación")
        print(err)

    finally:
        connect.close()
        print("Conexión finalizada de forma exitosa")
