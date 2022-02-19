import pymysql.cursors


def createDBConnection():
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="todolistdb",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def selectAllTasks() -> list:
    connection = createDBConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM todolistdb.tasks;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
