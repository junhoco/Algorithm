def solution(quizes):
    ans = []
    for quiz in quizes:
        quiz_ls = quiz.split()
        if quiz_ls[1] == '+':
            if int(quiz_ls[4]) == int(quiz_ls[0]) + int(quiz_ls[2]):
                ans.append('O')
            else:
                ans.append('X')
        else:
            if int(quiz_ls[4]) == int(quiz_ls[0]) - int(quiz_ls[2]):
                ans.append('O')
            else:
                ans.append('X')
    return ans