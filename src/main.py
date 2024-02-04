import uvicorn
from fastapi import FastAPI
from web import explorer, creature

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)


# starting uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
# run command `python main.py` in this directory