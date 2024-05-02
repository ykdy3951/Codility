# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    chk = [0] * (len(A) + 1)

    for i in A:
        chk[i - 1] = 1
    for i in range(len(A) + 1):
        if not chk[i]:
            return i + 1