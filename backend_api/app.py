from fastapi import FastAPI
import os
app = FastAPI()
@app.get("/")
def home():
    return {"message":"PhantomNet API Running"}
@app.get("/logs")
def get_logs():
    if not os.path.exists("phantomnet_agent/logs/attacks.log"):
        return {"logs":[]}
    with open("phantomnet_agent/logs/attacks.log") as f:
        return {"logs":f.readlines()}
