import requests

api_token = 'put token here'
api_url_base = 'https://ts.snipe-it.io/api/v1/hardware/'

headers = {'Content-Type': 'application/json',
            "Accept":"application/json",
           'Authorization': 'Bearer ' + str(api_token)
           }



def isCheckedOut(loanerNum):

    if loanerNum < 10:
        num = "0" + str(loanerNum)
    else:
        num = str(loanerNum)

    url = api_url_base + "?search=loaner" + num
    a = requests.get(url, headers = headers)
    jsonobj = a.json()
    rows = jsonobj.get('rows')
    for j in rows:
        if j.get('name') == "Loaner"+num:
            if (j.get("status_label").get("status_meta") == "deployed"):
                return True
            else:
                return False

num = 0
for i in range(1, 31):
    if isCheckedOut(i):
        num+=1
print(num)
