"""
This code checks whether the paranthesis are valid or not.
if so, it prints the each paranthesis pairs.
"""

n = int(input())
par = list(input())

def check(n, par):
    idxs = []
    stack = []
    valid = []
    for i in range(n):
        if par[i] == "(":
            par[i] = ""
            idxs.append(i+1)
            stack.append("(")
        else:
            if stack:
                stack.pop(-1)
                valid.append((idxs.pop(-1), i+1))
            else:
                return "not valid", stack, valid
    return "", stack, valid

mess, st, vl = check(n, par)
if mess == "":
    if st:
        print("not valid")
    else:
        print("valid")
        for i in sorted(vl):
            print(*i)
else:
    print("not valid")

"""
input)
    n = 8
    par = "(()(()))"
output)
    valid
    1 8
    2 3
    4 7
    5 6
"""