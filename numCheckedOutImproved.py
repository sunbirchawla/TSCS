import requests
import sys

api_token = str(sys.argv[1])
api_url_base = 'https://ts.snipe-it.io/api/v1/hardware/'

headers = {'Content-Type': 'application/json',
            "Accept":"application/json",
           'Authorization': 'Bearer ' + str(api_token)
           }



def isCheckedOut():
    url = api_url_base + "?search=Loaner&limit=150"
    a = requests.get(url, headers = headers)
    jsonobj = a.json()
    rows = jsonobj.get('rows')
    numOut = 0
    for j in rows:
        for loanerNum in range(1, 31):
            if loanerNum < 10:
                num = "0" + str(loanerNum)
            else:
                num = str(loanerNum)
            if j.get('name') == "Loaner"+num:
                if (j.get("status_label").get("status_meta") == "deployed"):
                    numOut += 1

    print(numOut)


isCheckedOut()
