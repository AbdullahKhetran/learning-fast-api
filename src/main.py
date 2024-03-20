import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from web import explorer, creature, user, file
from pathlib import Path
from typing import Generator


app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
# app.include_router(user.router)
app.include_router(file.router)


# Serving Static files
top = Path(__file__).parent

app.mount("/static",
          StaticFiles(directory=f"{top}/static", html=True),
          name="free")

# starting uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
# run this file

# to start from terminal; run `uvicorn main:app`
