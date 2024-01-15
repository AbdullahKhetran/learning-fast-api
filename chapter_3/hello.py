from fastapi import FastAPI, Body, Header

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
    return f"Hello? {who}?"


@app.post("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent


# Start Uvicorn internally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
