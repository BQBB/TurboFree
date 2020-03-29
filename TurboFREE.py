import requests
import re
req=lambda: requests.get('https://www.instagram.com').text
csrftoken=re.search('"csrf_token":"(.*?)",',req()).group(1)
i=0

def login(user,pas,token):
    req=requests.post('https://www.instagram.com/accounts/login/ajax/',data={'username':user,'password':pas,'queryParams': '{}',
'optIntoOneTap': 'false'},headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36','x-csrftoken':token})
    if '{"authenticated": false,' in req.text:
        return 'Fail'
    else:
        return req.cookies
def getallinfo(cookie):
    req=requests.get('https://www.instagram.com/accounts/edit/?__a=1',headers={'x-csrftoken':cookie['csrftoken']},cookies=cookie).text
    email=re.search('"email":"(.*?)",',req).group(1)
    bio=re.search('"biography":"(.*?)"',req).group(1)
    phone=re.search('"phone_number":"(.*?)"',req).group(1)
    return[email,bio,phone]
def change(user,email,cookie,bio='',phone=''):
    req=requests.post('https://www.instagram.com/accounts/edit/',data={'first_name':'', 'email':email  ,'username':user  ,'phone_number':phone, 'biography': bio ,'external_url': '','chaining_enabled': 'on'},headers={'x-csrftoken':cookie['csrftoken']},cookies=cookie).text
    if '{"status": "ok"}' in req:
        print('\n[+] New username : '+user)
        exit()
    else:
        print('\n[+] Fail username : ' + user )
        exit()
def search(user,email,cooki,bio,phone):
    global i
    req=requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',data={'email':'rdgee5e5h@gmail.com','password':'112233445566','first_name':'BQBB','username':user,'opt_into_one_tap':'false'},headers={'x-csrftoken':csrftoken})
    if '"dryrun_passed": true' in req.text:

        change(user,email,cooki,bio,phone)
    else:
        i=i+1
        print(f'\r[+] Search : {i}',end='')
        search(user,email,cooki,bio,phone)
def work():
    username = input('username : ')
    pas = input('password : ')
    cookie = login(username, pas, csrftoken)
    if cookie == 'Fail':
        work()
    else:
        target=input('target : ')
        info=getallinfo(cookie)
        search(target,info[0],cookie,info[1],info[2])





work()






