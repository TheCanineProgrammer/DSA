# This program uses binary search to check whether x is in the list or not if so, it returns the index of it otherwise returns -1

n = int(input())
A = list(map(int, input().split()))
r = n-1
l = 0
x = int(input())

def binary_search(A, l, r, x):
    i = (l+r) // 2
    if r < l:
        return -1
    mid = (l+r) // 2
    if A[mid] == x:
        return i
    elif A[mid] > x:
        i += 1
        return binary_search(A, l, mid - 1, x)
    else:
        i -= 1
        return binary_search(A, mid+1, r, x)

print(binary_search(A, l, r, x))

"""
input 1)
    5
    1 2 3 4 5
    6
output 1)
    -1

input 2)
    3
    432 751 753
    751
output 2)
    1
"""