# https://ru.stackoverflow.com/questions/1373486/%D0%9D%D1%83%D0%B6%D0%BD%D0%BE-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-%D1%81-cbr-ru-%D0%BF%D0%BE-%D0%BA%D1%83%D1%80%D1%81%D0%B0%D0%BC-%D0%B7%D0%B0-%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4?ysclid=llwevqda7f735994992

import pandas as pd

url = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=10/01/2022&date_req2=20/01/2022&VAL_NM_RQ=R01235'
results = pd.read_xml(url)

print(results)
