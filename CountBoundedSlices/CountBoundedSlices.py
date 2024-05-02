# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from heapq import heappush, heappop

def solution(K, A):
    # Implement your solution here
    max_heap, min_heap = [-A[0]], [A[0]]
    alen = len(A)
    fidx, sidx = 0, 0
    flag = False
    res = 0

    while fidx < alen and sidx < alen:
        if (-max_heap[0] - min_heap[0]) <= K:
            sidx += 1
            if sidx < alen:
                heappush(max_heap, -A[sidx])
                heappush(min_heap, A[sidx])
            flag = True
        else:
            if flag:
                n = sidx - fidx
                res += n * (n - 1) // 2
                flag = False
            
            temp = []
            while A[fidx] != (-max_heap[0]):
                temp.append(heappop(max_heap))
            heappop(max_heap)

            for i in temp:
                heappush(max_heap, i)
            
            temp = []
            while A[fidx] != min_heap[0]:
                temp.append(heappop(min_heap))
            heappop(min_heap)

            for i in temp:
                heappush(min_heap, i)

            fidx += 1

    if flag:
        n = sidx - fidx
        res += n * (n - 1) // 2
    
    return res + alen