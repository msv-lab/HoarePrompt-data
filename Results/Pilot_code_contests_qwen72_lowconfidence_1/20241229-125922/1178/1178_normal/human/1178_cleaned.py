def func_1():
    args = []
    for line in sys.stdin:
        args.append(line)
    return args

def func_2(word):
    n = len(word) - 2
    return word[0] + str(n) + word[n + 1]
argLines = func_1()
n = int(argLines[0])
argLines.pop(0)
for word in argLines:
    w = word.replace('\n', '')
    if len(w) > 10:
        print(func_2(w))
    else:
        print(w)