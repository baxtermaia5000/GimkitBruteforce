import requests as rq
import random as rand
from bs4 import BeautifulSoup as bs
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import warnings
warnings.filterwarnings("ignore", message="The input looks more like a filename than markup. You may want to open this file and pass the filehandle into Beautiful Soup.")
mode = input("Loud mode? y/n\n>>> ")
usef=input("Write to file? y/n\n>>> ")
code = input("Code? (leave blank)\n>>> ")
if code == "":
    code = "23123"
#seque=input("Sequential mode? (slower but more thoutough) y/n\n>>> ")
print("\n>>Press ctrl+c to stop program<<\n")
if usef=="y":
    file=open("hits.txt","w")
#checked=[]
try:
    while True:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': 'https://www.gimkit.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.gimkit.com/join',
            # 'Cookie': '__stripe_mid=32dcd2aa-4803-48c6-8fb4-110d7c415f1ddf56a4; __stripe_sid=c40e1442-e78a-40b3-9b38-c4b7706b489b62cc96',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }
        cookies = {
            '__stripe_mid': '69b3b857-0d9f-425d-a3b8-304a04be2dc12d8758',
        '_ga': 'GA1.1.1204632036.1702560656',
        '_ga_32KJCRTBF3': 'GS1.1.1702560656.1.1.1702561698.0.0.0',
        'connect.sid': 's%3AgzrofURXoCOWJRjH7lJjXzED3gHCDcPb.QTRedBHU%2BxrQKYaD8Dk%2Bx8QE2A%2BktYnIDH4iHCGuUUU',
        '__stripe_sid': '202d92f3-ea39-43bf-9865-956f827df7cc875273',
    }
        json_data = {
            'code': str(code),
        }
        #checked.append(code)
        if mode=="y":
            print(f'Searching {code}...')
        try:
            response = rq.post(
                'https://www.gimkit.com/api/matchmaker/find-info-from-code',
                cookies=cookies,
                headers=headers,
                json=json_data,
            )
        except rq.exceptions.ConnectionError:
            print(">>Connection failed; no internet connection<<")
            break
        if str(response)=="<Response [500]>":
            #print(str(response) + str(code))
            pass
        else:
            soup=bs(response.text,"html.parser")
            parsed=json.loads(soup.text)
            json_data1= {
                    'roomId' : parsed["roomId"],
                    'name' : "test",
                    'clientType': 'Gimkit \u2061\u200d\u200c\u2064\u2061\u200d\u2062\u200c\u2062\u200c\u200d\u2062\u200c\u200d\u2062\u200c\u2061\u2062\u2061\u200c\u200d\u2061\u200d\u200d\u2064\u2062\u200d\u2064\u2061\u200d\u2063\u2062\u2061\u2061\u200d\u2061\u200d\u200c\u2061\u2062\u2063\u2061\u200d\u200d\u200c\u2061\u200c\u2061\u2062\u200c\u2061\u2063\u200c\u2061\u2062\u2063\u2061\u2061\u200c\u2061\u2064\u2062\u200c\u200d\u2061\u2061\u2061\u200d\u200c\u2062\u2061\u200d\u2061\u2064\u2063\u200d\u2061\u200c\u2062\u200d\u2062\u200d\u200d\u200d\u2063\u200d\u2061\u200d\u2064\u200d\u2061\u2061\u2064\u200c\u2062\u2061\u2062\u200d\u200d\u2064\u200c\u2062\u2063\u200d\u2061\u200d\u2061\u200c\u2062\u2061\u2062\u2061\u200d\u200d\u2062\u200c\u2061\u200d\u200c\u2061\u2061\u2061\u2061\u2061\u2061\u2062\u200c\u2061\u2061\u2063\u200c\u2062\u200d\u2063\u2062\u200d\u2064\u2063\u2064\u2062\u200c\u2062\u200d\u200c\u200d\u2061\u200d\u2062\u200d\u2062\u200d\u200c\u2061\u200c\u200d\u2061\u2061\u200d\u2064\u2061\u200c\u2062\u200d\u200d\u2061\u2062\u200d\u200d\u2061\u2063\u2063\u2063\u2064\u200c\u2062\u200d\u200c\u200d\u2061\u2062\u200c\u2061\u2062\u2061\u2062\u200d\u200c\u2061\u2064\u2061\u200d\u200c\u2062\u200c\u2061\u2061\u2061\u200d\u2061\u200d\u2061\u2061\u200c\u2061\u2063\u2061\u200d\u200c\u2061\u2061\u2062\u200d\u200d\u200d\u200d\u2062\u2061\u200c\u200d\u2061\u200c\u200d\u2062\u2061\u200c\u2061\u200c\u2061\u200d\u200d\u2062\u200c\u2062\u2063\u2062\u2061\u2064\u2062\u200c\u2064\u200c\u2061\u2062\u200d\u200d\u2062\u200c\u2061\u200c\u2061\u200d\u200d\u2061\u2061\u2061\u2062\u200d\u200d\u200c\u2062\u2063\u2062\u200c\u200d\u200c\u200d\u2064\u200c\u2062\u200c\u200d\u2063\u200c\u200d\u2062\u200c\u2062\u2061\u200d\u2061\u2062\u200c\u200d\u200d\u2062\u2063\u2061\u200c\u200d\u2061\u2062\u200dWeb Client V3.1'
            }
            response1 = rq.post('https://www.gimkit.com/api/matchmaker/join', cookies=cookies, headers=headers, json=json_data1)
            soup1=bs(response1.text,'html.parser')
            parsed1=json.loads(soup1.text)
            print(parsed1)
            #browser=webdriver.Chrome()
            #browser.get("https://gimkit.com/join")
            #sleep(3)
            #codebox=browser.find_elements_by_class("sc-dMVFSy ksvqsy")
            #print(codebox)
            if usef=="y":
                file.write(f'{code}\n')
            print(response1.text)
            print(f'Success at {code}, random names {parsed["useRandomNamePicker"]}, game type {"quiz" if parsed1["source"]=="original" else "not a quiz"}')
        code = rand.randint(1000,999999)
        #else:
            #code += 1
            #if code >= 1000000:
                #print("Sequential mode finished")
                #break
        #while code in checked:
            #code=rand.randint(1000,999999)
            #print("rerolled dupe")
except KeyboardInterrupt:
    exit("\n>>Program stopped<<")
