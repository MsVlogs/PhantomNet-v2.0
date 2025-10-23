import random
attack_types = ["Port Scan","Brute Force","Malware Drop","SQL Injection","Ping Flood"]
def analyze_attack(payload):
    score = len(payload)+random.randint(0,50)
    return attack_types[score%len(attack_types)]
