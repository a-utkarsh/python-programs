import textwrap

def wrap(string, max_width):
    for i in range(0, len(string), max_width):
        print(i)
        print( "\n".join([string[i:i + max_width]]))

wrap("ABCDEFGHIJKLMNOPQRSTUVWXYZ",4)

