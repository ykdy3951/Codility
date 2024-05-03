# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A.sort()

    for i in range(len(A)-2):
        if A[i] <= 0:
            continue
        for j in range(i+1, len(A)-1):
            if A[i] + A[j] > A[j+1]:
                return 1
    return 0