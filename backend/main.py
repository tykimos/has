from fastapi import FastAPI, Form, Request, status, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn
from datetime import datetime
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static/static"), name="react_static")
templates = Jinja2Templates(directory="templates")

class Post(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: str

posts_db = []

@app.get("/", response_class=HTMLResponse)
async def index():
    try:
        return FileResponse('static/index.html')
    except FileNotFoundError:
        return templates.TemplateResponse('index.html', {"request": Request})

@app.get('/favicon.ico')
async def favicon():
    file_name = 'favicon.ico'
    file_path = './static/' + file_name
    return FileResponse(path=file_path, headers={'mimetype': 'image/vnd.microsoft.icon'})

@app.post('/hello', response_class=HTMLResponse)
async def hello(request: Request, name: str = Form(...)):
    if name:
        print('Request for hello page received with name=%s' % name)
        return templates.TemplateResponse('hello.html', {"request": request, 'name':name})
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return RedirectResponse(request.url_for("index"), status_code=status.HTTP_302_FOUND)

@app.get("/api/posts", response_model=List[PostResponse])
async def get_posts():
    return posts_db

@app.post("/api/posts", response_model=PostResponse)
async def create_post(post: Post):
    new_post = {
        "id": len(posts_db) + 1,
        "title": post.title,
        "content": post.content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    posts_db.append(new_post)
    return new_post

@app.get("/{full_path:path}", response_class=HTMLResponse)
async def serve_spa(full_path: str):
    if full_path.startswith("api/"):
        raise HTTPException(status_code=404, detail="API endpoint not found")
    
    if os.path.exists(f"static/{full_path}"):
        return FileResponse(f"static/{full_path}")
    
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html")
    
    return templates.TemplateResponse('index.html', {"request": Request})

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)

