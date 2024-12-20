def encode(alphabet):
    n_char = (ord(alphabet) - 97)
    return chr((n_char // 10) + 97) + chr((n_char % 10) + 97)

def input_func(input):
    result = ""
    for i in input:
        result += encode(i)

    return result
