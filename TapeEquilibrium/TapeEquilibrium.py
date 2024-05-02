# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    N = len(A)
    lsum = A[0]
    rsum = sum(A[1:])
    res = 100000001
    for i in range(1, N):
        res = min(res, abs(lsum-rsum))
        lsum += A[i]
        rsum -= A[i]
    return res