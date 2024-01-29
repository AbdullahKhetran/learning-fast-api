from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def top():
    return "top here"


# starting uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
