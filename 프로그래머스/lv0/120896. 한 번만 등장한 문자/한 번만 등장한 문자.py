def solution(s):
    dup_list = []
    if len(s) == 1:
        return s
    for i in range(len(sorted(s))):
        if sorted(s)[i-1] == sorted(s)[i]:
            dup_list.append(sorted(s)[i-1])
    a = sorted(s)
    for search in dup_list:
        a = [k.strip(search) for k in a]
    answer = ''.join(a).strip(" ")
    return answer