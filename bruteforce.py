import requests as rq
import random as rand
mode = input("Loud mode?\n>>> ")
#define stuff for request (cURL converter .com)
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
#open file and prep loop
file=open("hits.txt", "w")
code=79536
checked=[]

#MAIN LOOP

while True:
    #redefine code var for requests
    json_data = {
        'code': str(code),
    }
    #add code to list for duplicate rerolling
    checked.append(code)
    #print more shit if in loud mode
    if mode=="y":
        print(f'Searching {code}...')
    #send post data
    response = rq.post(
        'https://www.gimkit.com/api/matchmaker/find-info-from-code',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    #ignore if invalid, print and append to file if valid code
    if str(response)=="<Response [500]>":
        #print(str(response) + str(code))
        pass
    else:
        print(f'Success at {code}!')
        file.write(f'{code}\n')
    #reroll code using randint()
    code=rand.randint(0,999999)
    #Make sure new code isn't a duplicate
    while code in checked:
        code=rand.randint(0,999999)
        print("rerolled dupe")
