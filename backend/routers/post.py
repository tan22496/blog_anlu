import shutil
import string
import random

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from routers.schemas import PostBase, PostDisplay
from database.database import get_db
from database import db_post


router = APIRouter(
    prefix='/post',
    tags=['post']
)

@router.post('/')
def create(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)

@router.get('/all')
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return db_post.delete(id, db)

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    """
    Mục tiêu là tạo 1 endpoint dể ng dùng gửi file lên server, xử lý lưu trữ với trên file duy nhất để tránh trùng lặp
    - tạo thư mục lưu trữ: images/
    - khai báo endpoint sử dụng @router.post("/image") 
    với tham số image: UploadFile = File(...).
    - Tạo tên file duy nhất:
        + sử dụng thư viện string và random để tao 1 chuỗi ngẫu nhiên
        + chèn chuỗi này vào tên file gốc ()
    - lưu file vào server:
        + sử dụng shutil.copyfileobj để chéo data từ file up vào 1 file mới trên hệ thống (mở bằng chế độ wb)
        + trả về đường dẫn file dưới dạng JSON đê frontend có thể sử dụng
    """
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}


