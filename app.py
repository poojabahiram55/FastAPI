from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def print_message():
    return 'Hello World!'
