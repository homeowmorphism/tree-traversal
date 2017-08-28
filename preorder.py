from tree import * 

def pre_order(tree):
    if tree:
        print tree.data
        pre_order(tree.left_child)
        pre_order(tree.right_child)

pre_order(A)
