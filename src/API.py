import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
values = os.getenv("PASSWORD")
# keys = os.getenv("API_KEY")
# headers = {keys: values}


def conversion(i: Any) -> Any:
    """Функция конвертации"""
    amount = i["transaction amount"]
    code = i["transaction currency"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    payload: dict[str, str] = {}
    response = requests.get(url, headers={"apikey": values}, data=payload)
    return response