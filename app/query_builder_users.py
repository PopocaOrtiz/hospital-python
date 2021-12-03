from typing import Tuple, Union
from dataclasses import dataclass

from app.db import DB


@dataclass
class User:
    id: int
    firstname: str
    lastname: str


class QueryBuilderUsers:

    def __init__(self, user_id: int = None, limit: int = None, name_like: str = None):
        self.filters = {
            'user_id': user_id,
            'limit': limit,
            'name_like': name_like
        }

    def prepare_query(self) -> Tuple[str, dict]:

        sql = """
            where true
        """
        params = {}

        if self.filters['user_id']:
            sql += """
                and id = %(user_id)s
            """
            params['user_id'] = self.filters['user_id']

        if self.filters['name_like']:
            name_like = f"%{self.filters['name_like']}"

            sql += """
                and (
                    firstname like %(name_like)s
                    or
                    lastname like %(name_like)s
                )
            """

            params['name_like'] = name_like

        if self.filters['limit']:
            sql += """
                limit %(limit)s
            """
            params['limit'] = self.filters['limit']

        return sql, params

    def get(self) -> list[User]:

        sql, params = self.prepare_query()

        sql = f"""
            select
                id,
                firstName,
                lastName 
            from users
            {sql}
        """

        db = DB()

        users: list[User] = []
        for row in db.select(sql, params):
            users.append(
                User(
                    id=row['id'],
                    firstname=row['firstName'],
                    lastname=row['lastName']
                )
            )

        return users

    def get_one(self) -> Union[User, None]:

        self.filters['limit'] = 1

        users = self.get()

        return users[0] if users else None
