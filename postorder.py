from tree import *

def post_order(tree):
    if tree:
       post_order(tree.left_child)
       post_order(tree.right_child)
       print tree.data

post_order(A)
