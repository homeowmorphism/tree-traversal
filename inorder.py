from tree import *

def in_order(tree):
    if tree:
        in_order(tree.left_child)
        print tree.data
        in_order(tree.right_child)

in_order(A)
