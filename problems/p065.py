import sys

s = sys.stdin.readline().strip()
word = []
out = []
in_tag = False

for ch in s:
    if in_tag == True:
        out.append(ch)
        if ch == ">":
            in_tag = False  
    else:
        if ch == "<":
            if len(word) != 0:
                out.extend(reversed(word))
                word.clear()
            in_tag = True
            out.append(ch)
        elif ch == " ":
            if len(word) != 0:
                out.extend(reversed(word))
                word.clear()
            out.append(" ")
        else:
            word.append(ch)

if len(word) != 0:
    out.extend(reversed(word))

print("".join(out))