def solution(my_string):
    answer = []
    for s in my_string:
        if s in '0123456789':
            answer.append(int(s))
    return sorted(answer)