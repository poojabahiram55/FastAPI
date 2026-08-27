import uvicorn
from fastapi import FastAPI
from enum import Enum
from typing import Literal

app = FastAPI()

@app.get('/')
def print_message():
    return 'Hello World!'


@app.get('/user-details/{name}')
def user_details(name: str):
    return {
        'username': name
    }


# Normal path parameter validation using a manual if-condition.
@app.get('/items/{item_type}')
def item_details(item_type: str):
    if item_type in ['book', 'pen', 'notebook']:
        return {'message': f'You requested {item_type}'}
    else:
        return {'error': f'Invalid request {item_type}'}


class Stationary(Enum):
    book = 'Book'
    pen = 'Pen'
    notebook = 'Notebook'


# Enum-based path parameter validation with predefined allowed values.
@app.get('/stationary/{name}')
def stationary(name: Stationary):
    return {'message': f'You requested stationary {name}'}


@app.get('/colors/{color_name}')
def colors(color_name: Literal['red', 'green', 'blue']):
    return {'message': f'You requested {color_name}'}



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)