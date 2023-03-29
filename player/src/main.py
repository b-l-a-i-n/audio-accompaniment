from fastapi import FastAPI, Form, Request
from fastapi.responses import Response, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from utils import get_predictions
import logging
import json


app = FastAPI()

app.mount("/static", StaticFiles(directory='static', html=True), name='static')

templates = Jinja2Templates(directory='static')

@app.get("/", response_class=HTMLResponse)
def index_page(request: Request):
    #with open("static/index.html", "r") as f:
    #    index_page = f.read()
    #return Response(index_page , media_type="text/html")
    return templates.TemplateResponse('index.html', {'request': request})

@app.get("/static/{file_path}")
def get_file(file_path):
    print(file_path)
    return FileResponse('static/'+file_path)

@app.post("/audio/{film_id}/{time_stamp}")
def get_audio_description(film_id, time_stamp):

    # Fix it
    url = 'https://storage.googleapis.com/shaka-demo-assets/angel-one/video_576p_768k_vp9.webm'

    text = get_predictions(url, float(time_stamp))
    r = json.dumps({'predictions':text})
    print(r)
    return Response(content=r, media_type='application/json')

