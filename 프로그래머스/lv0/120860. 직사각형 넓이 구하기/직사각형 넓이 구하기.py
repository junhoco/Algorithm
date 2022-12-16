def solution(dots):
    new_dots = sorted(dots)
    print(new_dots)
    print(new_dots[1][0])
    x = new_dots[-1][0] - new_dots[0][0]
    print(x)
    y = new_dots[-1][1] - new_dots[-2][1]
    print(y)
    return x * y