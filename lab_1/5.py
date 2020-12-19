import requests
import xml.etree.ElementTree as ET

root_dollar = ET.fromstring(requests.get("http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/03/2020&date_req2=01/07/2020&VAL_NM_RQ=R01235").content)
root_euro = ET.fromstring(requests.get("http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/03/2020&date_req2=01/07/2020&VAL_NM_RQ=R01239").content)
root_indian_rupee = ET.fromstring(requests.get("http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/03/2020&date_req2=01/07/2020&VAL_NM_RQ=R01270").content)
root_ukrainian_hryvnia = ET.fromstring(requests.get("http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/03/2020&date_req2=01/07/2020&VAL_NM_RQ=R01720").content)

print("DATE\t\tDollar\tEuro\tIndian\tUkrainian hryvnia")

for x in range(len(root_dollar)):
    print(root_dollar[x].attrib['Date'], end='\t')
    print(root_dollar[x][1].text, end='\t')
    print(root_euro[x][1].text, end='\t')
    print(root_indian_rupee[x][1].text, end='\t')
    print(root_ukrainian_hryvnia[x][1].text)
