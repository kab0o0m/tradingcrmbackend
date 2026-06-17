from sqlalchemy import *
from database import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    pair = Column(String(20))
    direction = Column(String(10))
    strategy = Column(String(100))
    session = Column(String(50))

    risk_amount = Column(DECIMAL(10,2))
    pnl = Column(DECIMAL(10,2))

    entry_date = Column(Date)
    close_date = Column(DateTime)

    status = Column(String(50))

    comments = Column(Text)

    setup_grade = Column(
    String(10),
    nullable=True
)