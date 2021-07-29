from sqlalchemy.sql.schema import Column
from sqlalchemy.types import Integer, String
from skatebase.models.model import Base

class UserModel(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    def __repr__(self):
       return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
