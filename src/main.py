import uvicorn
from fastapi import FastAPI, File
from web import explorer, creature, user

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
# app.include_router(user.router)


@app.post("/small")
async def upload_small_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"


# starting uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
# run this file

# to start from terminal; run `uvicorn main:app`
