import sys

k,n,m = map(int,sys.stdin.readline().split())

price = k * n

if price > m :
    print(price - m)
elif price <= m:
    print(0)