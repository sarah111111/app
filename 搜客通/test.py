import requests
import re
import json
import json
import numpy as np

h = {
    'Cookie': 'PHPSESSID=9pdkr2ia5v4rb252qr8csel4s1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
}


def seach():
    for i in range(0, 401):
        url1 = 'https://www.souketong.com/clientSearch/clientsearch/search?charset=utf-8'
        params1 = {
            "p": i,
            "q": "建筑"
        }
        requests.packages.urllib3.disable_warnings()
        seach = requests.get(url=url1, headers=h, params=params1, verify=False)
        print(seach.text)
        clientsId = re.findall("class=\"width40-btn\" id=\'(.+?)'", seach.text)
        clientsId1 = re.findall('class=\"width40-btn\" id=\"(.+?)"', seach.text)

        url2 = 'https://www.souketong.com/clientSearch/clientsearch/import_clients?charset=utf-8'
        requests.packages.urllib3.disable_warnings()
        d = {
            "clientsId[]": clientsId1
        }

        add = requests.post(url=url2, headers=h, data=d, verify=False)
        print(add.text)


seach()
