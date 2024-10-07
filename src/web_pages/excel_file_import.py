import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

"""Функция,которая может получать данные их файлов Excel и импортировать их"""
def read_xlsx(file_path: str) -> list[dict]:
    transaction_list = []
    try:
        excel_data = pd.read_excel(file_path)
        len_, b = excel_data.shape
        for i in range(len_):
            if excel_data["Дата операции"][i]:
                transaction_list.append(
                    {
                        "transaction date": excel_data["Дата операции"][i],
                        "payment date": excel_data["Дата платежа"][i],
                        "card number": excel_data["Номер карты"][i],
                        "status": excel_data["Статус"][i],
                        "transaction amount": excel_data["Сумма операции"][i],
                        "transaction currency": excel_data["Валюта операции"][i],
                        "payment amount": excel_data["Сумма платежа"][i],
                        "payment currency": excel_data["Валюта платежа"][i],
                        "cashback": excel_data["Кэшбэк"][i],
                        "category": excel_data["Категория"][i],
                        "MCC": excel_data["MCC"][i],
                        "description": excel_data["Описание"][i],
                        "bonuses": excel_data["Бонусы (включая кэшбэк)"][i],
                        "rounding to the investment bank": excel_data["Округление на инвесткопилку"][i],
                        "amount of the operation with rounding": excel_data["Сумма операции с округлением"][i],

                    }
                )
            else:
                continue
    except Exception:
        return []
    return transaction_list




"""Проверка работы функции на примере файла operations.xlsx"""
if __name__ == "__main__":
    print(read_xlsx("../../data/operations.xlsx"))









