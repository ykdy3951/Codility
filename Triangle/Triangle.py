# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A.sort()
    res = 0
    for i in range(len(A)):
        if A[i] > 0:
            A = A[i:]
            break
    
    for i in range(0, len(A)-2):
        for j in range(i+1, len(A)-1):
            for k in range(j+1, len(A)):
                if A[i] + A[j] > A[k]:
                    res += 1
    return res