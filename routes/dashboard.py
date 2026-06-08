from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from models.trade import Trade
from models.account import Account
from models.user import User

from utils.auth import get_current_user

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("")
def dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    print("\n========== DASHBOARD ==========")
    print("Current User ID:", current_user.id)
    print("Current User Email:", current_user.email)

    account = (
        db.query(Account)
        .filter(
            Account.user_id == current_user.id
        )
        .first()
    )

    print("Account Found:", account)

    if account:
        print(
            "Current Balance:",
            account.current_balance
        )

        balance = (
            account.current_balance
        )
    else:
        balance = 0

    trades = (
        db.query(Trade)
        .filter(
            Trade.user_id ==
            current_user.id
        )
        .all()
    )

    total_trades = len(trades)

    wins = len([
        trade
        for trade in trades
        if trade.status == "SUCCESS"
    ])

    losses = len([
        trade
        for trade in trades
        if  trade.status == "FAIL"
    ])

    total_pnl = sum(
        trade.pnl
        for trade in trades
    )

    win_rate = (
        wins /
        (wins + losses)
        * 100
    )
        

    print(
        "Returning Balance:",
        balance
    )

    print("===============================\n")

    return {
        "balance": balance,
        "total_trades": total_trades,
        "wins": wins,
        "losses": losses,
        "win_rate": win_rate,
        "total_pnl": total_pnl
    }