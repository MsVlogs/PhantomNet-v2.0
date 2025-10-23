import socket, threading, json
from utils.logger import log_event
from utils.crypto import encrypt_data
from ai_analyzer import analyze_attack

CONFIG = json.load(open("phantomnet_agent/config.json"))

def honeypot_listener(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", port))
    s.listen(5)
    print(f"[+] Honeypot active on port {port}")
    while True:
        conn, addr = s.accept()
        data = conn.recv(2048).decode(errors="ignore")
        log_event(addr[0], port, data)
        encrypted = encrypt_data(data)
        prediction = analyze_attack(data)
        print(f"[!] Attack from {addr[0]}:{port} | Type: {prediction}")
        conn.close()

def start_honeypots():
    ports = CONFIG["ports"]
    for port in ports:
        t = threading.Thread(target=honeypot_listener, args=(port,))
        t.daemon = True
        t.start()
    print("[*] PhantomNet Agent started...")
    input("Press Enter to stop.\n")

if __name__ == "__main__":
    start_honeypots()
