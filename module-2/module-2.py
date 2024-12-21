
def input_func(input):
    result = ""
    for i in range(0, len(input), 2):
        n_char = str((ord(input[i]) - 97)) + str((ord(input[i + 1]) - 97))
        result += chr(int(n_char) + 97)

    return result
