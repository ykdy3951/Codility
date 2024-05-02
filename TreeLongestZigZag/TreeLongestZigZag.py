# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task

def solution(T):
    # Implement your solution here

    # 0 is left, 1 is right
    def traversal(sub_tree, prev_dir):
        if not sub_tree:
            return -1

        if prev_dir == 0:
            return max(traversal(sub_tree.l, 0), 1+traversal(sub_tree.r, 1))
        elif prev_dir == 1:
            return max(1+traversal(sub_tree.l, 0), traversal(sub_tree.r, 1))
        else:
            return max(traversal(sub_tree.l, 0), traversal(sub_tree.r, 1))

    return traversal(T, -1)