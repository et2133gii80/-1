from pandas.core.interchange.dataframe_protocol import DataFrame
import datetime
from datetime import datetime, timedelta, strptime
import datetime






date = datetime.datetime.today()
date_now = date.strftime("%d-%m")



def range_time(date: str, mouth: int = 1) -> list:
    """
    находит диапазон дат в радиусе месяца
    :param mouth: диапазон
    :param date: дата и время в формате YYYY-MM-DD HH:MM:SS
    :return: список с датами в формате M D Y
    """
    base = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    date_list = []
    for _ in range(mouth):
        b1 = int(base.strftime("%m"))
        b = int(base.strftime("%m"))

        while b == b1:
            date_list.append(base.strftime("%m %d %Y"))
            base = base - timedelta(days=1)
            b = int(base.strftime("%m"))

        return date_list

def spending_by_category(df: DataFrame, category: str, date: str = date_now):
    list_time = range_time(date, 3)
    amount_list=[]
    sum=0

    for i in df:
        if i["category"] == category and i["transaction date"] in list_time :
            amount_list.append(i["transaction amount"])
    for s in amount_list:
        sum+=s
        return sum

    # transactions = transactions[transactions["Сумма платежа"] < 0]
    # if date is None:
    #     date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # list_time = range_time(date, 3)
    # logger.info("find category...")
    # transactions = find_category_df(transactions, category)
    # logger.info("find time range...")
    # transactions = find_range_time_df(transactions, list_time)
    # logger.info("done")
    # return json.dumps(transactions.to_json(force_ascii=False, orient="records"), ensure_ascii=False)

