from fastapi import FastAPI
from .web import explorer

app = FastAPI()

app.include_router(explorer.router)


@app.get("/")
def top():
    return "top here"


@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"


# starting uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
# run command `python main.py` in this directory
