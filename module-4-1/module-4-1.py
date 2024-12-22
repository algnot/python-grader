
def input_func(input):
    start , end = map(int, input.split(":"))
    sum = 0
    for i in range(start, end+1):
        sum += i

    return sum
