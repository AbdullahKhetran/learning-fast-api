from fastapi import FastAPI, Body, Header, Response

app = FastAPI()


# @app.get("/hi")
# def greet():
#     return "Hello? World?"

# # URL Path
# @app.get("/hi/{who}")
# def greet(who: str):
#     return f"Hello {who.capitalize()}"


# # Query Parameters
# @app.get("/hi")
# def greet(who: str):
#     return f"Hello {who.capitalize()}"


# # Body - POST request
# @app.post("/hi")
# def greet(who: str = Body(embed=True)):
#     return f"Hello {who.capitalize()}"


# HTTP Header
@app.post("/hi")
def greet(who: str = Header()):
    return f"Hello {who.capitalize()}"


@app.post("/agent")
def get_agent(user_agent: str = Header()):
    return f"agent is '{user_agent}'"


@app.get("/happy")
def happy(status_code=200):
    return ":)"


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"


# Start Uvicorn internally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
