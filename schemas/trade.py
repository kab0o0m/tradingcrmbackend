from pydantic import BaseModel

from datetime import date

class TradeCreate(BaseModel):
    pair: str
    direction: str
    strategy: str
    session: str
    risk_amount: float
    pnl: float
    status: str
    entry_date: date
    comments: str

class TradeUpdate(BaseModel):
    pair: str
    direction: str
    strategy: str
    session: str
    risk_amount: float
    pnl: float
    status: str
    entry_date: date
    comments: str