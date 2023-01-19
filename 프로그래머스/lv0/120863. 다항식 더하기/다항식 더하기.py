def solution(polynomial):
    sums = [0,0]
    for var in polynomial.split():
        if var == '+':
            pass
        elif var == 'x':
            sums[0] += 1
        elif 'x' in var:
            sums[0] += int(var[:-1])
        else:
            sums[1] += int(var)

    res = ''
    if not sums[0] == 0:
        if sums[0] == 1:
            res += 'x'
        else:
            res += str(sums[0]) + 'x'
    if not sums[1] == 0:
        if not res == '':
            res += ' + '
        res += str(sums[1])
    return res
