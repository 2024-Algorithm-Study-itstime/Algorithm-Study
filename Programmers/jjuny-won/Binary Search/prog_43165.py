def solution(numbers, target):

    current_sums = [numbers[0], -numbers[0]]
    for num in numbers[1:]:
        next_sums = []
        for s in current_sums:
            next_sums.append(s + num)
            next_sums.append(s - num)
        current_sums = next_sums
    
    return current_sums.count(target)

