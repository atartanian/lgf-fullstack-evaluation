from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UnicodeText
from sqlalchemy.orm import relationship

from .database import Base


class TodoList(Base):
    __tablename__ = "todo_list"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    items = relationship("ListItem", back_populates="list")

class ListItem(Base):
    __tablename__ = "list_item"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(UnicodeText)
    list_id = Column(Integer, ForeignKey("users.id"))
    parent_item_id = Column(Integer, ForeignKey("list_item.id"))

    list = relationship("TodoList", back_populates="items")
    parent = relationship("ListItem", back_populates="children")
    children = relationship("ListItem", back_populates="parent")
