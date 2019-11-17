import textwrap

def wrap(string, max_width):
    output = ""
    for i in range(0, len(string), int(max_width)):
        output = output + string[i:i + max_width] + "\n"
    return output


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
