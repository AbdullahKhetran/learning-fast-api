from fastapi import FastAPI, Body

app = FastAPI()


@app.post("/hi")
def greet(who: str = Body(embed=True)):
    return f"Hello {who}"


# Starting Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)

# Now visit `http://127.0.0.1:8000/docs` to access automated documentation
