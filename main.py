from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from db import DB
from query_builder_users import QueryBuilderUsers

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/users")
async def get_users():

    users = QueryBuilderUsers().get()

    return {
        'users': users
    }


@app.get("/users/{user_id}")
async def get_user(user_id: int):

    user = QueryBuilderUsers(user_id).get_one()

    return {
        'user': user
    }


class User(BaseModel):
    id: int
    firstname: str
    lastname: str


@app.post('/users')
async def create_user(user: User):

    sql = """
        insert into users
        (firstName, lastName)
        values
        (%(firstname)s, %(lastname)s)
    """

    new_id = DB().insert(sql, dict(user))

    user.id =new_id

    return {
        'user': user
    }


@app.put('/users/{user_id}')
def update_user(user_id: int, user: User):

    sql = """
        update users
        set firstname = %(firstname)s,
            lastname = %(lastname)
        where id = %(user_id)s
    """

    user = dict(user)
    user['user_id'] = user_id

    DB().update(sql, user)

    return {
        'user': user
    }



if __name__ == '__main__':
    print(QueryBuilderUsers(1).get_one())