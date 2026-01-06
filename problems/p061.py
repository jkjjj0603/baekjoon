import sys

n,m = map(int,sys.stdin.readline().split())

prices = []
for _ in range(m):
    price = int(sys.stdin.readline().strip())
    prices.append(price)

prices.sort()

best_profit = 0
best_price = 0

for i in range(m):
    price = prices[i]
    buyers = m - i
    sold = min(n,buyers)
    profit = price * sold

    if profit > best_profit:
        best_profit = profit
        best_price = price

print(f"{best_price} {best_profit}")