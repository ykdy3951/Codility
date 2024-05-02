# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict
def solution(A):
    # Implement your solution here
    d = defaultdict(int)

    for i in A:
        d[i] = (d[i]+1) % 2
    
    for key in d.keys():
        if d[key]:
            return key