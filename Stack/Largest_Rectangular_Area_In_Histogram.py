n = int(input())
hist = list(map(int, input().split()))
area = 0
stack = []

for i in range(n+1):
    current = hist[i] if i < n else 0
    
    while stack and current < hist[stack[-1]]:
        h = hist[stack.pop()]
        width = i if not stack else i - stack[-1] - 1
        area = max(area, h * width)
    
    stack.append(i)

print(area)