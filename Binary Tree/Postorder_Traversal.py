# A code to find the post-order traversal of a Binary Tree with the pre-order and in-order traversals given

def find_postorder(preorder, inorder):
    
    if not preorder or not inorder:
        return []

    root = preorder[0]
    root_index_in_order = inorder.index(root)

    left_inorder = inorder[:root_index_in_order]
    left_preorder = preorder[1 : len(left_inorder) + 1]

    right_inorder = inorder[root_index_in_order + 1:]
    right_preorder = preorder[len(left_inorder) + 1:]

    postorder_left = find_postorder(left_preorder, left_inorder)
    postorder_right = find_postorder(right_preorder, right_inorder)

    return postorder_left + postorder_right + [root]

inorder = [4, 2, 5, 1, 3, 6]
preorder = [1, 2, 4, 5, 3, 6]

print(find_postorder(preorder, inorder))