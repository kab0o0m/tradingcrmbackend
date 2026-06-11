from decimal import Decimal

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.trade import (
    TradeCreate,
    TradeUpdate
)

from models.trade import Trade
from models.user import User
from models.account import Account

from utils.auth import get_current_user

router = APIRouter(
    prefix="/trades",
    tags=["Trades"]
)


@router.post("")
def create_trade(
    trade: TradeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    print("Incoming Trade:")
    print(trade.model_dump())

    new_trade = Trade(
        user_id=current_user.id,

        pair=trade.pair,
        direction=trade.direction,
        strategy=trade.strategy,
        session=trade.session,

        risk_amount=trade.risk_amount,
        pnl=trade.pnl,

        status=trade.status,
        entry_date=trade.entry_date,

        comments=trade.comments
    )

    db.add(new_trade)

    account = (
        db.query(Account)
        .filter(
            Account.user_id ==
            current_user.id
        )
        .first()
    )

    if account:
        account.current_balance += Decimal(str(trade.pnl))

    db.commit()

    db.refresh(new_trade)

    return {
        "id": new_trade.id,
        "pair": new_trade.pair
    }


@router.get("")
def get_trades(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    trades = (
        db.query(Trade)
        .filter(
            Trade.user_id ==
            current_user.id
        ).order_by(
        Trade.entry_date.desc(),
        Trade.id.desc()
    )
        .all()
    )

    return trades

@router.get("/recent")
def get_recent_trades(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    trades = (
        db.query(Trade)
        .filter(
            Trade.user_id == current_user.id
        )
        .order_by(
            Trade.entry_date.desc(),
            Trade.id.desc()
        )
        .limit(5)
        .all()
    )

    return trades


@router.get("/{trade_id}")
def get_trade(
    trade_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    trade = (
        db.query(Trade)
        .filter(
            Trade.id == trade_id,
            Trade.user_id == current_user.id
        )
        .first()
    )

    if not trade:
        return {
            "message": "Trade not found"
        }

    return {
        "id": trade.id,
        "pair": trade.pair,
        "entry_date": trade.entry_date,
        "direction": trade.direction,
        "strategy": trade.strategy,
        "session": trade.session,
        "risk_amount": float(trade.risk_amount),
        "pnl": float(trade.pnl),
        "status": trade.status,
        "comments": trade.comments
    }


@router.put("/{trade_id}")
def update_trade(
    trade_id: int,
    trade_data: TradeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    trade = (
        db.query(Trade)
        .filter(
            Trade.id == trade_id,
            Trade.user_id == current_user.id
        )
        .first()
    )

    if not trade:
        return {
            "message": "Trade not found"
        }

    old_pnl = Decimal(
        str(trade.pnl)
    )

    new_pnl = Decimal(
        str(trade_data.pnl)
    )

    trade.pair = trade_data.pair
    trade.direction = trade_data.direction
    trade.strategy = trade_data.strategy
    trade.session = trade_data.session

    trade.risk_amount = trade_data.risk_amount
    trade.pnl = trade_data.pnl

    trade.entry_date = trade_data.entry_date
    trade.status = trade_data.status
    trade.comments = trade_data.comments


    pnl_difference = (
        new_pnl -
        old_pnl
    )

    account = (
        db.query(Account)
        .filter(
            Account.user_id ==
            current_user.id
        )
        .first()
    )

    if account:
        account.current_balance += pnl_difference

    account = (
        db.query(Account)
        .filter(
            Account.user_id ==
            current_user.id
        )
        .first()
    )

    if account:
        account.current_balance += pnl_difference

    db.commit()

    return {
        "message": "Trade updated"
    }


@router.delete("/{trade_id}")
def delete_trade(
    trade_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    trade = (
        db.query(Trade)
        .filter(
            Trade.id == trade_id,
            Trade.user_id == current_user.id
        )
        .first()
    )

    if not trade:
        return {
            "message": "Trade not found"
        }

    account = (
        db.query(Account)
        .filter(
            Account.user_id ==
            current_user.id
        )
        .first()
    )

    if account:
        account.current_balance -= Decimal(str(trade.pnl))

    db.delete(trade)

    db.commit()

    return {
        "message": "Trade deleted"
    }