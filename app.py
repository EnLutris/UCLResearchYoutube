from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Literal
import os
from utils.youtube_comments import get_youtube_comments
from fastapi import FastAPI, File, UploadFile
import re


port = os.environ.get('PORT', 8000)
app = FastAPI(PORT = port)

@app.get("/")
async def status_check():
  return "alive"

@app.post("/uploadfile/")
async def process(file: UploadFile = File(...)):
    
    if not file:
        return {"message": "No upload file sent"}
    else:
        content = await file.read()
        url_list = re.split(',', content.decode('utf-8'))
        comment_list = []
        for url in url_list:
           comments = get_youtube_comments(url)
           comment_list.append(comments)
        return comment_list
          
    
@app.post("/comments")
async def youtube_comments(url: str):
  print(url)
  comments = get_youtube_comments(url)
  return comments
