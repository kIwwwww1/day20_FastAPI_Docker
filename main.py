import uvicorn
from fastapi import FastAPI

app = FastAPI()

users = [
    {'id': 1, 'name': 'Danil'},
    {'id': 2, 'name': 'Eva'},
    {'id': 3, 'name': 'Dima'},
    {'id': 4, 'name': 'Kirill'},
]

@app.get('/users')
def get_all_users():
    return users

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)