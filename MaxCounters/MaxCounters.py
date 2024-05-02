# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    l = [0] * N
    max_cnt = 0
    update = 0

    for i in A:
        if i != N + 1:
            l[i-1] = max(update, l[i-1])+1
            max_cnt = max(max_cnt, l[i-1])
        else:
            update = max_cnt
    for i in range(N):
        if l[i] < update:
            l[i] = update
    return l