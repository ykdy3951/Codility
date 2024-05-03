# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    MAX_VAL = 10000000
    st, end = [], []
    for i in range(len(A)):
        st.append(i-A[i])
        end.append(i+A[i])
    
    st.sort()
    end.sort()
    res, j = 0, 0
    for i in range(len(end)):
        while j < len(st) and st[j] <= end[i]:
            j+=1
        res += j - i - 1
        if res > MAX_VAL:
            return -1
    return res