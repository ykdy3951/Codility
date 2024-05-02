
# TreeLongestZigZag

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

In this problem we consider binary trees. Let's define a <i>turn</i> on a path as a change in the direction of the path (i.e. a switch from right to left or vice versa). A <i>zigzag</i> is simply a sequence of turns (it can start with either right or left). The length of a zigzag is equal to the number of turns.
Consider binary tree below:
<img class="inline-description-image" src="https://codility-frontend-prod.s3.amazonaws.com/media/task_static/tree_longest_zig_zag/static/images/auto/02cfce1572f250aa1fb5d31feba5da94.png">
There are two turns on the marked path. The first one is at [15]; the second is at [30]. That means that the length of this zigzag is equal to 2. This is also the longest zigzag in the tree under consideration. In this problem you should find the longest zigzag that starts at the root of any given binary tree and form a downwards path.
Note that a zigzag containing only one edge or one node has length 0.

Problem

Write a function:
<p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>def solution(T)</tt></p>
that, given a non-empty binary tree T consisting of N nodes, returns the length of the longest zigzag starting at the root.
For example, given tree T shown in the figure above, the function should return 2, as explained above. Note that the values contained in the nodes are not relevant in this task.

Technical details

A binary tree can be specified using a pointer data structure. Assume that the following declarations are given:
<p style="font-family: monospace; font-size: 9pt; display: block; white-space: pre-wrap"><tt>from dataclasses import dataclass, field

@dataclass
class Tree:
    x: int = 0
    l: "Tree" = None
    r: "Tree" = None</tt></p>
An empty tree is represented by an empty pointer (denoted by <tt style="white-space:pre-wrap">None</tt>). A non-empty tree is represented by a pointer to an object representing its root. The attribute <tt style="white-space:pre-wrap">x</tt> holds the integer contained in the root, whereas attributes <tt style="white-space:pre-wrap">l</tt> and <tt style="white-space:pre-wrap">r</tt> hold the left and right subtrees of the binary tree, respectively.
For the purpose of entering your own test cases, you can denote a tree recursively in the following way. An empty binary tree is denoted by <tt style="white-space:pre-wrap">None</tt>. A non-empty tree is denoted as (X, L, R), where X is the value contained in the root and L and R denote the left and right subtrees, respectively. The tree from the above figure can be denoted as:
  (5, (3, (20, (6, None, None), None), None), (10, (1, None, None), (15, (30, None, (9, None, None)), (8, None, None))))

Assumptions

Write an <b><b>efficient</b></b> algorithm for the following assumptions:
<ul style="margin: 10px;padding: 0px;"><li>N is an integer within the range [<span class="number">1</span>..<span class="number">100,000</span>];</li>
<li>the height of tree T (number of edges on the longest path from root to leaf) is within the range [<span class="number">0</span>..<span class="number">800</span>].</li>
</ul>


