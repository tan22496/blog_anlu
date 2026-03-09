from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
import datetime

from routers.schemas import PostBase
from database.models import DbPost


## xây dựng logic tại Database Layer

def create(db: Session, request: PostBase):
    """
    hàm xử lý việc lưu trữ dữ liệu
    db:
    request: chứa dữ liệu bài đăng
    """
    new_post = DbPost(
        image_url=request.image_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        timestamp=datetime.datetime.now()
    )
    ### thực hiện các bước chuẩn của SQLAlchemy 
    ### thêm đối tượng vào session, commit lưu thay đổi vào DB
    ### refresh: Cập nhập lại đối tượng để lấy các dữ liệu tự sinh (như 'id')
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db: Session):
    """
    sử dụng db.query(DBPost).all() 
    để truy xuất toàn bộ bản ghi có trong bảng `Post`
    """
    return db.query(DbPost).all()

def delete(id: int, db: Session):
    """3 bước
    - tìm kiếm bản ghi cần xoá
    - kiểm tra tồn tại: ko có báo 404
    - thực thi: thực hiện delete , commit để xác nhận thay đổi vào database
    """
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with {id} not found')
    db.delete(post)
    db.commit()
    return 'ok'


