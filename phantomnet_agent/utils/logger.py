import datetime, os
def log_event(ip, port, data):
    os.makedirs("logs", exist_ok=True)
    with open("logs/attacks.log", "a") as f:
        f.write(f"{datetime.datetime.now()} | IP:{ip} | Port:{port} | Data:{data}\n")
