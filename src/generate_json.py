import json

from pandas import DataFrame


def generate_json(data:DataFrame)->str:
    with open("..data/operations.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file)

