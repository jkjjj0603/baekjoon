import sys

sound = sys.stdin.readline().strip()
max_duck = 0
states = []
pos = {"q" : 0, "u" : 1, "a" : 2, "c" : 3, "k" : 4}

for ch in sound:
    if ch not in pos:
        print(-1)
        sys.exit()
    
    step = pos[ch]

    if ch == "q":
        reused = False
        for i in range(len(states)):
            if states[i] == 4:
                states[i] = 0
                reused = True
                break
        if not reused:
            states.append(0)
        if len(states) > max_duck:
            max_duck = len(states)

    else:
        target = step - 1
        found = False
        for i in range(len(states)):
            if states[i] == target:
                states[i] = step
                found = True
                break
        if not found:
            print(-1)
            sys.exit()
if not states or any(s != 4 for s in states):
    print(-1)
else:
    print(max_duck)

