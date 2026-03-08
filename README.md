# blog_anlu

python = 3.12.9
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# git 
## tao nhanh
git branch dev
### xoa nhanh
git branch -d dev
## chuyen nhanh
git checkout -b dev


# 

- open giao diện tài liệu của FastAPI (Swagger UI)
- ex: gửi 1 ycau POST với dữ liệu mẫu
    + kq: trả về mã `200 ok` kèm theo dữ liệu bài đăng có đầy đủ id và timestamp vừa đk tạo trong database.

- 

## hd cách xay dựng tính năng tạo bài đăng post mới vào cơ sở dữ liệu bằng FastAPI và SQLAlchemy
### 1. Xây dựng logic tại Database Layer (db_post.py)
- hàm create để xử lý việc lưu trữ dữ liệu
+ tham số: nhận vào đối tượng db và request (chứa dữ liệu bài đăng)
+ xử lý: Khởi tạo 1 đối tg DBPost mới với các trường: image_url, title, content, creator và tự động tạo timestamp bằng datetime.now().
+ lưu trữ: thực hiện các bước chuẩn của SQLAlchemy:
++ add: thêm đối tg vào session.
++ commit: lưu thay đổi vào DB
++ refresh: cập nhập lại đối tượng để lấy các dữ liệu tự sinh (như `id`)

### 2. Tạo API Router (post.py)
- thiết lập điêm cuối (endpoint) để ng dùng có thể gọi từ giao diện tài liệu (Docs):
+ Khởi tạo APIRouter với tiền tố `/post` và gắn thẻ (tag) để phân loại trong Swagger UI.
+ đ/n pthuc @router.post(''):
    + sử dụng Depends(get_db) để kết nối với database
    + gọi hàm db_post.create đã viết ở b1 để xử lý logic.

## 3. tích hợp vào ứng dụng chính (main.py)
- Để các router mới hoạt động, chúng cần đk đăng ký với app FastAPI chính
+ import router từ file `post.py`
+ sử dụng `app.include_router(post.router)` để kích hoạt các endpoint của bài đăng.




