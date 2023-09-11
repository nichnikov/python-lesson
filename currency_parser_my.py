# https://ru.stackoverflow.com/questions/1373486/%D0%9D%D1%83%D0%B6%D0%BD%D0%BE-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D1%81-cbr-ru-%D0%BF%D0%BE-%D0%BA%D1%83%D1%80%D1%81%D0%B0%D0%BC-%D0%B7%D0%B0-%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4?ysclid=llwevqda7f735994992
# https://www.cbr.ru/development/sxml/ описание данных
import pandas as pd
import locale
from locale import atof
import datetime


date_in = "01/01/2023"
date_out = "11/09/2023"
nm_rq = "R01375"

url = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={}&date_req2={}&VAL_NM_RQ={}'.format(date_in, date_out, nm_rq)
exchange_rates_df = pd.read_xml(url)
exchange_rates_df["Date"] = pd.to_datetime(exchange_rates_df["Date"], dayfirst=True)
exchange_rates_df["Month"] = exchange_rates_df["Date"].apply(lambda x: x.month)

locale.setlocale(locale.LC_NUMERIC, '')
exchange_rates_df["Value"] = exchange_rates_df["Value"].apply(lambda x: atof(x))

print(exchange_rates_df)
exchange_rates_df.to_csv("results.tsv", sep="\t", index=False)


print(exchange_rates_df)
print(exchange_rates_df['Value'].mean())

average_by_month_df = exchange_rates_df.groupby('Month', as_index=False)['Value'].mean()

print(average_by_month_df)
# average_by_month_df.to_excel("currencies_average_by_month.xlsx")

with pd.ExcelWriter ("currencies.xlsx") as writer:
    exchange_rates_df.to_excel(writer, sheet_name="exchange_rates")
    average_by_month_df.to_excel(writer, sheet_name="monthly_average_exchange_rates")