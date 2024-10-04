import datetime
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
import re
import os


def hello_user()->str:
    """Функиия, которая выводит приветствие в зависимости от текущего времени"""
    date = datetime.datetime.today()
    date_now = date.strftime("%H")

    list_of_dict= [
        {"Доброй ночи":"000102030405"},
        {"Доброе утро":"06070809101112"},
        {"Добрый день":"13141516"},
        {"Добрый вечер":"17181920212223"}
    ]
    for dict in list_of_dict:
        for key in dict:
            if date_now in dict[key]:
                return key



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




def card_numder(df:DataFrame)-> list:
    """Функция, которая возвращает номера карт без повторов"""
    card_list=[]
    for i in df:
        card_list.append(i["card number"])
    filter_list=[]
    for card in card_list:
        if card not in filter_list and card != "nan":
            filter_list.append(card)
    return filter_list
# filter list =['*7197', '*5091', nan, '*4556', '*1112', '*5507', '*6002', '*5441']


# Напишем функцию, которая будет считать траты и кэшбек для каждой карты

def card_namber_sum (df:DataFrame, filter_list:list)-> list:
    sum_dict ={}
    sum= 0
    sum_payment_amount_list = []
    for i in df:
        if i["transaction currency"] == "RUB":
            if i["card number"] == filter_list[0]:
                sum_payment_amount_list.append(i["amount of the operation with rounding"])
    for sum1 in sum_payment_amount_list:
        sum +=sum1

    dict_sum={filter_list[0]: round(sum,1)}
    return dict_sum















def sum (df:DataFrame)->str:
    sum_payment_amount = 0
    cashback = sum_payment_amount/100
    sum_payment_amount_list=[]
    for i in df:
        if i["card number"] == df[0]["card number"]:
            if i["transaction currency"]== "RUB":
                sum_payment_amount_list.append(i["transaction amount"])
            else:
                conversion_amount=conversion(i)
                sum_payment_amount_list.append(conversion_amount)
    for amount in sum_payment_amount_list:
        sum_payment_amount+= amount
    return sum_payment_amount
    #     else:
    #         pass
    # return sum_payment_amount_list

# """Путь до excel файла"""
# current_excel = os.path.dirname(os.path.abspath(__file__))
# rel_excel_file_path = os.path.join(current_excel, "../data/operations.xlsx")
# excel_file_path = os.path.abspath(rel_excel_file_path)
#
#
# # """Проверка работы функции на примере файла operations.xlsx"""
# # def main():
# #     df= read_xlsx(excel_file_path)
# #     print(card_number(df))
# #
# # if __name__ =="__main__":
# #     main()
#
