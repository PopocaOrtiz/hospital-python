from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


if __name__ == '__main__':
    print(QueryBuilderUsers(1).get_one())