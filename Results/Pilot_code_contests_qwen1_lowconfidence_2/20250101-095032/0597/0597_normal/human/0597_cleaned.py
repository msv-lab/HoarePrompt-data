input = sys.stdin
output = sys.stdout
MAX = 10 ** 6
Da = 'Dasha'
Ma = 'Masha'

def func_1(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

def func_2(a, b):
    assert a * b / func_1(a, b) == a / func_1(a, b) * b
    return a / func_1(a, b) * b

def func_3(numbers):
    return reduce(lambda a, b: func_1(a, b), numbers)

def func_4(numbers):
    return reduce(lambda a, b: func_2(a, b), numbers)

def func_5(n):
    return n * (n + 1) / 2

def func_6(a, b):
    G = func_1(a, b)
    L = func_2(a, b)
    if a < b:
        M = (L / b - 1) * G
        D = L - M
        if D > M:
            return Ma
        else:
            return Da
    else:
        M = (L / a - 1) * G
        D = L - M
        if D > M:
            return Ma
        else:
            return Da
S = input.readline().split(' ')
a = int(S[0])
b = int(S[1])
assert 1 <= a and a <= MAX
assert 1 <= b and b <= MAX
assert a != b
answer = func_6(a, b)
output.write('%s\n' % answer)