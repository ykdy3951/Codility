# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A = list(set(A))
    A.sort()
    for i in range(len(A)):
        if A[i] <= 0:
            continue
        else:
            A = A[i:]
            break
    if A == []:
        return 1
    for i in range(len(A)):
        if A[i] != i+1:
            return i+1
    return len(A) + 1