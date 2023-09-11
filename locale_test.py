import locale
from locale import atof

locale.setlocale(locale.LC_NUMERIC, '')
str_num = "1,55"
num_f = atof("1,55")
print(num_f, type(num_f))