from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from database import Base

class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    starting_balance = Column(
        DECIMAL(12,2)
    )

    current_balance = Column(
        DECIMAL(12,2)
    )