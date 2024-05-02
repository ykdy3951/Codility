# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    N = len(A)
    for i in range(1, N):
        A[i] += A[i-1]
    res = A[N-1]
    for i in range(1,N):
        res = min(abs(A[i-1]*2-A[N-1]),res)
    return res