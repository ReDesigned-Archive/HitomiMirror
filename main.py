from fastapi import FastAPI
from starlette.responses import StreamingResponse
import utils
import ziputil

logger = utils.getLogger("MAIN")
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def testzip():
    res = ziputil.zipfiles(r"C:\test")
    return res