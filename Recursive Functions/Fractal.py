import sys
import numpy as np
import matplotlib.pyplot as plt
sys.setrecursionlimit(10**7)

n, k = map(int, input().split())
pattern = [list(map(lambda x : 1 if x == "." else 0, input())) for _ in range(n)]

size = n ** k

def is_black(x, y, level):
    if level == 0:
        return False
    
    block_size = n ** (level - 1)
    px = x // block_size
    py = y // block_size
    
    if pattern[px][py] == 0:
        return True
    else:
        return is_black(x % block_size, y % block_size, level -1)

output = []

for i in range(size):
    row = []
    for j in range(size):
        if is_black(i, j, k):
            row.append(0)
        else:
            row.append(1)
    output.append(row)

output = np.array(output)

plt.imshow(output, cmap = "gray")
plt.title("Fractal")
plt.show()

"""
Example)
    n, k = 2, 3
    pattern = [[".", "*"], [".", "."]]                      "." stands for white and "*" stands for black
"""