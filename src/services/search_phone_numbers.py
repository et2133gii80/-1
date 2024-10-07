import json

from pandas import DataFrame
import os

def search_phone(df:DataFrame)-> list:
    """Функция возвращает JSON со всеми транзакциями, содержащими в описании мобильные номера """
    description_list = []
    for i in df:
        description_list.append(i["description"])

    phone_str = "+7"
    phone_list=[]
    for phone_description in description_list:
        if phone_str in phone_description:
            phone_list.append(phone_description)

    non_repeat_phone_description =[]
    for non_repeat in phone_list:
        if non_repeat not in non_repeat_phone_description:
            non_repeat_phone_description.append(non_repeat)

    #data_json_services= json.dumps(non_repeat_phone_description)
    # """Путь до json файла"""
    # current_json = os.path.dirname(os.path.abspath(__file__))
    # rel_json_file_path = os.path.join(current_json, "../data/operations.json")
    # json_file_path = os.path.abspath(rel_json_file_path)

    with open("../data/operations.json", "w", encoding = "utf-8") as json_file :
        data_json_services =json.dump(non_repeat_phone_description , json_file, ensure_ascii=False)

    return data_json_services





# def read_xlsx(file_path: str) -> list[dict]:
#     transaction_list = []
#     try:
#         excel_data = pd.read_excel(file_path)
#         len_, b = excel_data.shape
#         for i in range(len_):
#             if excel_data["Дата операции"][i]:
#                 transaction_list.append(
#                     {
#                         "transaction date": excel_data["Дата операции"][i],
#                         "payment date": excel_data["Дата платежа"][i],
#                         "card number": excel_data["Номер карты"][i],
#                         "status": excel_data["Статус"][i],
#                         "transaction amount": excel_data["Сумма операции"][i],
#                         "transaction currency": excel_data["Валюта операции"][i],
#                         "payment amount": excel_data["Сумма платежа"][i],
#                         "payment currency": excel_data["Валюта платежа"][i],
#                         "cashback": excel_data["Кэшбэк"][i],
#                         "category ": excel_data["Категория"][i],
#                         "MCC": excel_data["MCC"][i],
#                         "description ": excel_data["Описание"][i],
#                         "bonuses": excel_data["Бонусы (включая кэшбэк)"][i],
#                         "rounding to the investment bank": excel_data["Округление на инвесткопилку"][i],
#                         "amount of the operation with rounding": excel_data["Сумма операции с округлением"][i],
#
#                     }
#                 )
#             else:
#                 continue
#     except Exception:
#         return []
#     return transaction_list