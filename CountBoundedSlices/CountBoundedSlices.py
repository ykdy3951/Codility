# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    # Implement your solution here
    MAX_INT = 1000000000
    alen = len(A)

    maxq, minq = [0] * (alen + 1), [0] * (alen + 1)
    max_pos, min_pos = [0] * (alen + 1), [0] * (alen + 1)

    fmax, lmax, fmin, lmin, = 0, -1, 0, -1

    j, res = 0, 0

    for i in range(alen):
        while j < alen:
            while lmax >= fmax and maxq[lmax] <= A[j]:
                lmax -= 1
            lmax += 1
            maxq[lmax] = A[j]
            max_pos[lmax] = j
        
            while lmin >= fmin and minq[lmin] >= A[j]:
                lmin -= 1
            lmin += 1
            minq[lmin] = A[j]
            min_pos[lmin] = j

            if (maxq[fmax] - minq[fmin] <= K):
                j += 1
            else:
                break
        res += (j - i)
        if min_pos[fmin] == i:
            fmin += 1
        if max_pos[fmax] == i:
            fmax += 1

    return min(MAX_INT, res)