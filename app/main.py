from fastapi import FastAPI

app = FastAPI()

@app.get("/api/system/status")
def status():
    return {"mode": "PRIVATE_GOLD", "market_state": "WAIT", "confidence_threshold": 80}

@app.get("/api/signals/latest")
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