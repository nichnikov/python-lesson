# https://gist.github.com/artkpv/3cbff1819846a4eec132be21a1fbd63d
# curl 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='$DATE -s |  grep -Po $CURR'.*?Value>[^<]*' | sed -En -e 's/.*>([0-9,]*)/\1/gp' -
import requests

DATE="02/03/2002"
CURR="USD"

