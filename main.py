from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    id: int
    title: str
    bode: str


posts = [
    {'id': 1, "title": 'news 1', 'body': 'text 1'},
    {'id': 2, "title": 'news 2', 'body': 'text 2'},
    {'id': 3, "title": 'news 3', 'body': 'text 3'}
]


@app.get('/items')
async def items() -> List:
    post_objects = []
    for post in posts:
        post_objects.append(Post(id=post['id'], title=post['title'], body=post['body']))
    return post_objects
