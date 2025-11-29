from fastapi import FastAPI, Depends, HTTPException
import uvicorn

from routers import blogs, user,authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blogs.router)

@app.get('/')
def firct_page():
    return {'msg': "This is the first page"}


if __name__ == "__main__":
    uvicorn.run('main:app',host = "127.0.0.1",port = 8000,reload = True)