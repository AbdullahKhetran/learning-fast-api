from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/hi")
async def greet():
    await asyncio.sleep(1)
    return "Hello? World?"

# start uvicorn using this command: uvicorn greet_async:app

# The only difference from a synchronous function that used the standard
# sleep(1) function is that the web server can handle other requests in the
# meantime with the async example.
