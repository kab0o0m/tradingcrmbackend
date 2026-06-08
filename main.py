from fastapi import FastAPI

from database import Base
from database import engine

from models.user import User
from models.account import Account
from models.trade import Trade

from routes.auth import router as auth_router
from routes.trades import router as trade_router
from routes.dashboard import router as dashboard_router

from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.include_router(auth_router)
app.include_router(trade_router)
app.include_router(dashboard_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "Trading CRM API"
    }

