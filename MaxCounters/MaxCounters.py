# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    l = [0] * N
    max_cnt = 0

    for i in A:
        if i == N + 1:
            l = [max_cnt] * N
        else:
            l[i-1]+=1
            max_cnt = max(max_cnt, l[i-1])
    return l