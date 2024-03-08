import uvicorn
from fastapi import FastAPI
from web import explorer, creature, user

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
# app.include_router(user.router)


# starting uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
# run this file

# to start from terminal; run `uvicorn main:app`
