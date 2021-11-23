import pymysql.cursors


class DB:

    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='pruebas',
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_cursor(self) -> pymysql.cursors.DictCursor:
        return self.connection.cursor()

    def select(self, sql: str, params: dict = None) -> list[dict]:

        if params is None:
            params = {}

        cursor = self.get_cursor()
        cursor.execute(sql, params)
        return cursor.fetchall()