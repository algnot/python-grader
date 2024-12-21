
def input_func(input):
    x, y, n = map(int, input.split(":"))

    first = (x + n - 1) // n * n
    last = y // n * n

    if first > y:
        return 0

    return (last - first) // n + 1
