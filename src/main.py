from src.web_pages.web_pages import card_numder, card_namber_sum
from src.web_pages.excel_file_import import read_xlsx
import os
from src.services.search_phone_numbers import search_phone
from src.reports import spending_by_category

"""Путь до excel файла"""
current_excel = os.path.dirname(os.path.abspath(__file__))
rel_excel_file_path = os.path.join(current_excel, "../data/operations.xlsx")
excel_file_path = os.path.abspath(rel_excel_file_path)


def main():
    df= read_xlsx(excel_file_path)
    # filter_list=card_numder(df)
    # print(card_namber_sum(df, filter_list))
    #search_phone(df)
    print(spending_by_category(df, "Супермаркеты", "18.09.21"))



if __name__ =="__main__":
    main()

