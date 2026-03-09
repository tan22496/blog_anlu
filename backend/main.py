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

### cấu hình truy cập file tĩnh (Static Files)
### mount thư mục: việc này giúp biến 1 thư mục nội bộ thành 1 tài nguyên có thể truy cập công khai qua HTTP.
app.mount('/images', StaticFiles(directory='images'), name='images')


# cấu ình CORS (Cross-origin Resource Sharing) để chuẩn bị cho việc kết nối với ứng dụng frontend (React)
## khi run ca FastAPI (Server) va React (Client) tren cung 1 may tinh nhung o 2 port khac nhau , trinh duyet se chan cacs ycau tu client den server vi bao mat (chinh sach Same-Origin Policy).
origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # danh sach cac domain dk phep
    allow_credentials=True, # cho phep gui kem cookie or thong tin xac thuc
    allow_methods=["*"], # cho phep tat cac pthuc (get, post, put, del)
    allow_headers=["*"] # cho phep tat ca cac headers.
)

# run : uvicorn main:app --reload