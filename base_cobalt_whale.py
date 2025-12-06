import requests, time

def cobalt_whale():
    print("Base — Cobalt Whale Detected (> 500 ETH moved in one tx on Coinbase L2)")
    seen = set()
    while True:
        r = requests.get("https://base.blockscout.com/api/v2/transactions?filter=validated")
        for tx in r.json().get("items", [])[:30]:
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            value = int(tx.get("value", 0)) / 1e18
            if value >= 500:  # > 500 ETH on Base
                print(f"COBALT WHALE SWAM\n"
                      f"{value:,.1f} ETH moved on Coinbase L2\n"
                      f"From: {tx['from']['hash'][:12]}...\n"
                      f"To:   {tx['to']['hash'][:12]}...\n"
                      f"Tx: https://basescan.org/tx/{h}\n"
                      f"→ Either Coinbase internal, Circle, or real institution\n"
                      f"→ Base just handled nation-state money with zero drama\n"
                      f"{'-'*85}")
        time.sleep(2.3)

if __name__ == "__main__":
    cobalt_whale()
