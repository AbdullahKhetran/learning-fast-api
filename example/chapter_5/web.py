# web.py - FastAPI endpoint

from model import Creature
from fastapi import FastAPI

app = FastAPI()


@app.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()


# Start Uvicorn internally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web:app", reload=True)


# or run `uvicorn web:app` to start server
