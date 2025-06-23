# A code to determine whether the given binary-tree is BST or not. without using OOP


n = int(input())                              # Number of Nodes
values = list(map(int, input().split()))      # Key values
keys = [0] + values

tree = {} 
for i in range(1, n+1):                       # each node's left and right children
    l, r = map(int, input().split())
    tree[i] = [l if l != -1 else None, r if r != -1 else None]         # constructing the tree using dictionary

def find_root(tree):
    has_parent = set()
    for node in tree:
        l, r = tree[node]
        if l is not None:
            has_parent.add(l)
        if r is not None:
            has_parent.add(r)
    for node in range(1, n+1):
        if node not in has_parent:
            return node
    return None

def is_valid_bst_recursive(tree, node, min_val, max_val):
    if node is None:
        return True
    val = keys[node]
    if not (min_val < val < max_val):
        return False
    left, right = tree[node]
    return (is_valid_bst_recursive(tree, left, min_val, val) and
            is_valid_bst_recursive(tree, right, val, max_val))

root = find_root(tree)
if root is None:
    print("Yes" if n == 0 else "No")
else:
    if is_valid_bst_recursive(tree, root, float('-inf'), float('inf')):
        print("Yes")
    else:
        print("No")