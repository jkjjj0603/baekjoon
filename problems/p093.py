import sys

t = int(sys.stdin.readline().strip())

for x in range(1,t+1):
    words = []
    m = int(sys.stdin.readline().strip())
    for _ in range(m):
        word = sys.stdin.readline().strip()
        words.append(word)
    n = int(sys.stdin.readline().strip())
    print(f"Scenario #{x}:")
    for _ in range(n):
        data = list(map(int,sys.stdin.readline().split()))
        k = data[0]
        nums = data[1:]
        result = ""
        for idx in nums:
            result += words[idx]
        print(result)
    print()
            
        