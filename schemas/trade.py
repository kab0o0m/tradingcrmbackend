from pydantic import BaseModel

class TradeCreate(BaseModel):
    pair: str
    direction: str
    strategy: str
    session: str
    risk_amount: float
    pnl: float
    status: str
    comments: str

class TradeUpdate(BaseModel):
    pair: str
    direction: str
    strategy: str
    session: str
    risk_amount: float
    pnl: float
    status: str
    comments: str