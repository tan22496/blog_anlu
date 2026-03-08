from pydantic import BaseModel, ConfigDict
from datetime import datetime

### tạo schemas cho API
### sử dụng pydantic để kiểm soát dữ liệu ip,op (Data Validation)
class PostBase(BaseModel):
    image_url: str
    title: str
    content: str
    creator: str

class PostDisplay(BaseModel):
    id: int
    image_url: str
    title: str
    content: str
    creator: str
    timestamp: datetime
    ## cấu hình quan trọng: orm_mode=true để pydantic có thể đọc dữ liệu trực tiếp từ các đối tượng SQLAlchemy (ORM)
    # class Config():
    #     orm_mode = True
    model_config = ConfigDict(from_attributes=True)

