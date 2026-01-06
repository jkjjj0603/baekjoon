import sys

n = int(sys.stdin.readline().strip())
stack = []
for _ in range(n):

    command = sys.stdin.readline().strip()

    if command.startswith("push"):
        push_lst = command.split()
        stack.append(int(push_lst[1]))

    elif command == "pop":  
         if len(stack) != 0:
             num = stack.pop()
             print(num)
         elif len(stack) == 0:
             print(-1)
             
    elif command == "size":
        size = len(stack)
        print(size)
    
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif command == "top":
        if len(stack) != 0:
            top_num = stack[-1]
            print(top_num)
        elif len(stack) == 0:
            print(-1)