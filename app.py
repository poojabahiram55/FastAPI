from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def print_message():
    return 'Hello World!'

@app.get('/user-details/{name}')
def user_details(name: str):
    return {
        'username': name
    }
