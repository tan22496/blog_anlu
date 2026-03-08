from fastapi import FastAPI

from database import models
from database.database import engine
from routers import post

app = FastAPI()

app.include_router(post.router)

## lệnh tự động tạo file database .db và các bảng tương ứng khi app run
## sử dụng tool (TablePlus) để kết nối vào file blog_api.db và 
## xác nhận bảng post đã được tạo thành công với đầy đủ các cột
models.Base.metadata.create_all(engine)

# run : uvicorn main:app --reload