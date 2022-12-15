def solution(numbers):
    new_numbers = sorted(numbers)
    return max(new_numbers[0] * new_numbers[1] , new_numbers[-2] * new_numbers[-1])