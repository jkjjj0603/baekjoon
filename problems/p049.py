import sys

low = 1
high = 10

while True:
    guess = int(sys.stdin.readline().strip())
    if guess == 0:
        break
    hint = sys.stdin.readline().strip()

    if hint == "too high":
        high = min(high,guess - 1)
    elif hint == "too low":
        low = max(low,guess + 1)
    elif hint == "right on":
        if guess <= high and guess >= low:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        low = 1
        high = 10 