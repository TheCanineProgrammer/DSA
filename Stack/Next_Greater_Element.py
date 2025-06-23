n = int(input())
l = list(map(int, input().split()))

def nge(l, n):
    result = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        current = l[i]
        while stack and stack[-1] <= current:
            stack.pop()
        if stack:
            result[i] = stack[-1]
            
        stack.append(current)
    return result

print(*nge(l, n))