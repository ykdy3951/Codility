# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # Implement your solution here
    chk = [0] * X
    res = 0
    for i in range(len(A)):
        if not chk[A[i]-1]:
            chk[A[i]-1] = 1
            res += 1
        if res == X:
            return i
    return -1