def recursion_sum(numbers, *args):
    if args:
        sum_args = numbers
        for num in args:
            sum_args += num
        return sum_args

    if not numbers:
        return 0
    if isinstance(numbers, list):
        total = 0
        for i in numbers:
            total += recursion_sum(i)
        return total
    else:
        return numbers
