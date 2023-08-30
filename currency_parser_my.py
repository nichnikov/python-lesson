# https://ru.stackoverflow.com/questions/1373486/%D0%9D%D1%83%D0%B6%D0%BD%D0%BE-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D1%81-cbr-ru-%D0%BF%D0%BE-%D0%BA%D1%83%D1%80%D1%81%D0%B0%D0%BC-%D0%B7%D0%B0-%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4?ysclid=llwevqda7f735994992
# https://www.cbr.ru/development/sxml/ описание данных
import pandas as pd
import datetime


date_in = "01/01/2023"
date_out = "30/08/2023"
nm_rq = "R01235"

url = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={}&date_req2={}&VAL_NM_RQ={}'.format(date_in, date_out, nm_rq)
results = pd.read_xml(url)
results["Date"] = pd.to_datetime(results["Date"], dayfirst=True)
results["Month"] = results["Date"].apply(lambda x: x.month)

print(results)
# print([type(d) for  d in list(results["Date"])])
# print([datetime.datetime.strptime(d, "%d.%m.%Y") for  d in list(results["Date"])])
