# FastAPI
Learn FastAPI

# Introduction
A Python framework for building web APIs

An API is a web server, a continuously running software application on the web that responds to requests.

API is an acronym for "application programming interface."

# History
Developed and maintained by Sebastian Ramirez

First released in 2018 and still in active development

Over 100000 stars on GitHub

Over 20 million daily downloads on PyPi

Used by companies including Uber, Netflix, Amazon, Meta, and OpenAPI

# Features
Validates data payloads coming into and out of the server

Parses query parameters, path parameters, cookies, headers, and more

Optimized for speed (both in terms of performance and developer iteration)

Generates automatic Swagger/OpenAPI documentation from your code

# FastAPI vs The competition
FastAPI has overtaken both Django and Flask in daily downloads.

FastAPI is not as full-featured as a full framework like Django.

The developer is responsible for assembling the pieces of the application(database
interaction, models, validations, testing, file structure, etc.)

# Foundations
FastAPI is built upon two other Python libraries.

Starlette is the underlying asynchronous framework that enables the FastAPI web server.

Pydantic is a data validation library. It both verifies that data fits an expected shape and contorts it to
fit the expected shape–

# Install UV
https://docs.astral.sh/uv/getting-started/installation/#installation-methods
```commandline
curl -LsSf https://astral.sh/uv/install.sh | sh
```
# Upgrade UV
```commandline
uv self update
```

# Reformat code
```commandline
uv run ruff format
```

# Clients and Servers
## Clients
The client is the computer that initiates a request.

A request is an ask for data.

The request may come from a web application, a mobile app, a
command-line, and more.

## Servers
The Server is the computer that responds to the request, usually
with a payload of data.

FastAPI builds the server-side(backend) logic.

FastAPI maps the request to a corresponding route.

# Route and Endpoints

A route is a specific path that the server recognizes and 
maps to a procedure

A server needs to know what resource the client is requesting.

An endpoint is another word for route.

# HTTP

The HyperText Transfer Protocol (HTTP) is a web standard,
a set of rules for how clients and servers send and receive data

An HTTP request includes a route and an HTTP verb,
also called an HTTP method.

The HTTP method describes the type of request.

Most common type is GET request, the GET HTTP method/verb
indicates a request to fetch data

The server responds to a GET request by returning
one or more records.

The server may raise an error if the requested resource
cannot be found.  


# HTTP Codes
200 ok
201 Created

Status code in the 400 family represents client errors
400, 404, 401

Status code in the 500 family represents server errors.
500, 503

# Modes and Run fastapi server
## Development modes
Optimized for developers
```commandline
uv run fastapi dev
uv run fastapi dev app.py
uv run fastapi dev backend/app.py
```

## Production modes
Optimized for end Users

# Query Parameters
Query parameters are key-value pairs at the end of a route.

Query parameters allow the client to hit the same endpoint but customize the request.

A common use case is filtering server records based on or more criteria.


#### Install fastapi
```commandline
pip install fastapi
```

#### Install uvicorn
```commandline
pip install fastapi uvicorn
```

#### Run code
```commandline
uvicorn app:app --reload
```

# Important command
```commandline
command  shift  E
```