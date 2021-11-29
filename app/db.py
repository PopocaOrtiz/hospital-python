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

    def execute(self, params, sql):
        if params is None:
            params = {}

        cursor = self.get_cursor()
        affected_rows = cursor.execute(sql, params)

        return cursor, affected_rows

    def select(self, sql: str, params: dict = None) -> list[dict]:
        cursor, _ = self.execute(params, sql)
        return cursor.fetchall()

    def insert(self, sql: str, params: dict) -> int:
        cursor, _ = self.execute(params, sql)
        self.connection.commit()

        return cursor.lastrowid

    def update(self, sql: str, params: dict = None):
        _, rows_updated = self.execute(sql, params)
        self.connection.commit()

        return rows_updated
