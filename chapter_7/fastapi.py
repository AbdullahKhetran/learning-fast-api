# this shows comparsion between FastAPI and Flask, check flask.py file

from fastapi import FastAPI, Header

app = FastAPI()


# Path
@app.get("/hi/{who}")
def greet(who: str):
    return f"Hello {who}"


# Query Parameter
# who will be passed after the ? in url
@app.get("/hi")
def greet2(who):
    return f"Hello {who}"


# Body
@app.get("/hi")
def greet3(who):
    return f"Hello {who}"


# Header
@app.get("/hi")
def greet4(who: str = Header()):
    return f"Hello {who}"
