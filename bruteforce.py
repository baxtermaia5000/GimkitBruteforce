import requests as rq
import random as rand
from bs4 import BeautifulSoup as bs
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
mode = input("Loud mode? y/n\n>>> ")
usef=input("Write to file? y/n\n>>> ")
cookies = {
    '__stripe_mid': '32dcd2aa-4803-48c6-8fb4-110d7c415f1ddf56a4',
    '__stripe_sid': 'c40e1442-e78a-40b3-9b38-c4b7706b489b62cc96',
}

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
if usef=="y":
    file=open("hits.txt","w")
code=79536
checked=[]
while True:
    json_data = {
        'code': str(code),
    }
    checked.append(code)
    if mode=="y":
        print(f'Searching {code}...')
    response = rq.post(
        'https://www.gimkit.com/api/matchmaker/find-info-from-code',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    
    if str(response)=="<Response [500]>":
        #print(str(response) + str(code))
        pass
    else:
        soup=bs(response.text,"html.parser")
        parsed=json.loads(soup.text)
        #browser=webdriver.Chrome()
        #browser.get("https://gimkit.com/join")
        #sleep(3)
        #codebox=browser.find_elements_by_class("sc-dMVFSy ksvqsy")
        #print(codebox)
        if usef=="y":
            file.write(f'{code}\n')
        print(f'Success at {code} with random names {parsed["useRandomNamePicker"]}')
    code = rand.randint(0,999999)
    while code in checked:
        code=rand.randint(0,999999)
        print("rerolled dupe")

