from fastapi import HTTPException
from models.Blog_model import Blog_bs


def create_new_blog(blog,db):
    new_blog = Blog_bs(title=blog.title,body=blog.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_all_blogs(db):
    blog = db.query(Blog_bs).all()
    if not blog:
        raise HTTPException(status_code=404,detail=f"No ID is available")
    return blog

def get_blog_by_id(id:int,db):
    blog = db.query(Blog_bs).filter(Blog_bs.id == id).first()
    if not blog:
        raise HTTPException(status_code=404,detail=f"Id {id} is not currently available")
    return blog

def update_blog_by_id(id:int,blog,db):
    updated_blog = db.query(Blog_bs).filter(Blog_bs.id == id)
    if not updated_blog.first():
        raise HTTPException(status_code=404,detail=f"Id {id} is not currently available")
    updated_blog.update(blog.dict())
    db.commit()
    return updated_blog.first()

def delete_blog_by_id(id:int,db):
    deleted_blog = db.query(Blog_bs).filter(Blog_bs.id == id)
    if not deleted_blog.first():
        raise HTTPException(status_code=404,detail=f"Id {id} is not currently available")
    deleted_blog.delete()
    db.commit()
    return f"Blog {id} is deleted"