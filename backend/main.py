from fastapi import FastAPI

from database import models
from database.database import engine
from routers import post
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(post.router)

## lệnh tự động tạo file database .db và các bảng tương ứng khi app run
## sử dụng tool (TablePlus) để kết nối vào file blog_api.db và 
## xác nhận bảng post đã được tạo thành công với đầy đủ các cột
models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')

origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# run : uvicorn main:app --reload