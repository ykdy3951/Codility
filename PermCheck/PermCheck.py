# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    N = len(A)
    chk = [0] * N
    for i in A:
        if N < i or chk[i-1]:
            return 0
        chk[i-1] = 1
    return 1