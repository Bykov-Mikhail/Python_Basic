def sorting_with_condition(numbers):
    for i in numbers:
        if i != round(i):
            return numbers
    else:
        return sorted(numbers)
