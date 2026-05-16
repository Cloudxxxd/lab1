from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/info")
def get_info():
    today = datetime.now()
    new_year = datetime(year=today.year + 1, month=1, day=1)
    delta = new_year - today

    return {
        "days_before_new_year": delta.days
    }