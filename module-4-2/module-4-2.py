
def input_func(input):
    start , end = map(int, input.split(":"))
    n = end - start + 1

    return (n / 2) * (2*start + (n-1))
