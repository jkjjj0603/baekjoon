import sys

n,m = map(int,sys.stdin.readline().split())

min_package = 1000
min_single = 1000

for _ in range(m):
    package_price, single_price = map(int,sys.stdin.readline().split())
    if min_package > package_price:
        min_package = package_price
    if min_single > single_price:
        min_single = single_price

only_single_cost = n * min_single
only_package_cost = (n + 5) // 6 * min_package
mixed_cost = (n // 6) * min_package + (n % 6) * min_single

answer = min(only_single_cost,only_package_cost,mixed_cost)

print(answer)