from fastapi import APIRouter

router = APIRouter()

@router.get("/system/status")
def status():
    return {
        "mode": "PRIVATE_GOLD",
        "market_state": "WAIT",
        "confidence_threshold": 80
    }

@router.get("/signals/latest")
def latest_signal():
    return {
        "pair": "XAUUSD",
        "direction": "BUY",
        "entry": 2036.4,
        "sl": 2028.1,
        "tp1": 2048.0,
        "confidence": 89,
        "timeframe": "M15",
        "session": "London-NY"
    }

@router.get("/stats/performance")
def performance():
    return {
        "win_rate": 64.2,
        "avg_rr": 2.3,
        "total_trades": 37
    }
