import requests
url = "https://api.binance.com/api/v3/ticker/24hr"
payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
response = response.json()
top_3 = [[''], [''], ['']]
def find_top3(usa):
    symbol = ''
    vol = 0
    for i in range(len(response)):
        if response[i]['symbol'] != usa[0][0]:
            if response[i]['symbol'] != usa[1][0]:
                if float(response[i]['volume']) > vol:
                    symbol = response[i]['symbol']
                    vol = float(response[i]['volume'])
    return [symbol, vol]
for j in range(3):
    top_3.insert(j, find_top3(top_3))
    del top_3[j+1]
for k in range (len(top_3)):
    print('Name:',top_3[k][0],'\n''Volume is:',top_3[k][1])