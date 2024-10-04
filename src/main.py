from src.web_pages.web_pages import card_number
from src.web_pages.excel_file_import import read_xlsx
import os

"""Путь до excel файла"""
current_excel = os.path.dirname(os.path.abspath(__file__))
rel_excel_file_path = os.path.join(current_excel, "../data/operations.xlsx")
excel_file_path = os.path.abspath(rel_excel_file_path)


# def main():
#     df= read_xlsx(excel_file_path)
#     print(card_number(df))
#
# if __name__ =="__main__":
#     main()
