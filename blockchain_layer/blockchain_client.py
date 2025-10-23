import hashlib, json
def submit_to_ledger(ip,port,data):
    tx={"ip":ip,"port":port,"hash":hashlib.sha256(data.encode()).hexdigest()}
    print("[Ledger] Transaction:",json.dumps(tx,indent=2))
