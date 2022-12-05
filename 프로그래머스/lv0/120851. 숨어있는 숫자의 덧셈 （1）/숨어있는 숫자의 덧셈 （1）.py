def solution(my_string):
    res = 0
    for s in my_string:
        if s.isdigit():
            res += int(s)
    return res