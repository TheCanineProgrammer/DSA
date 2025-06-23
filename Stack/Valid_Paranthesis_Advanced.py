n = int(input())
s = input()

def check(n, s):
    stack = []
    
    for i in range(n):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            stack.append(s[i])
        else:
            if stack:
                if s[i] == "]" and stack[-1] == "[":
                    stack.pop(-1)
                elif s[i] == "}" and stack[-1] == "{":
                    stack.pop(-1)
                elif s[i] == ")" and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return "not valid", stack
            else:
                return "not valid", stack
    return "", stack

message, stack = check(n, s)

if message == "":
    if stack:
        print("not valid")
    else:
        print("valid")
else:
    print(message)

"""
input 1)
    n = 8
    s = "[{}([])]"
output 1)
    valid

input 2)
    n = 6
    s = "[{]}()"
output 2)
    not valid
"""