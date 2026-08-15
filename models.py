from sqlalchemy import Column, Integer, String

from database import Base


class MenuItem(Base):

    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True)

    category = Column(String)

    name = Column(String)

    price = Column(String)