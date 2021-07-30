from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models.model import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import Integer, String


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = UserModel
        load_instance = True

    id = auto_field()
    name = auto_field()
    fullname = auto_field()
