from fastapi import FastAPI

app = FastAPI()


# @app.get("/hi")
# def greet():
#     return "Hello? World?"

# URL Path
@app.get("/hi/{who}")
def greet(who: str):
    return f"Hello {who.capitalize()}"


# Start Uvicorn internally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
