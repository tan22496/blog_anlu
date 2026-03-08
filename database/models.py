from .database import Base
from sqlalchemy import Column, Integer, String, DateTime


### Định nghĩa Model database
class DbPost(Base):
    """
    sử dụng sqlalchemy để đ/n cấu trúc bảng trong DB
    """
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    title = Column(String)
    content = Column(String)
    creator = Column(String)
    timestamp = Column(DateTime)





