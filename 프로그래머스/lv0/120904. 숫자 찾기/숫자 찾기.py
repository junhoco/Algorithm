def solution(num, k):
    for idx, val in enumerate(str(num)):
        if val == str(k):
            return (idx+1)
    return -1