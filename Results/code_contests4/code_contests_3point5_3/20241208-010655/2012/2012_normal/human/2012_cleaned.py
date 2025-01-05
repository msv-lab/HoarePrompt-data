a = raw_input()
b = raw_input()
i = 0
j = 0
allen = len(a)
bllen = len(b)
while i < allen and a[i] == '0':
    i += 1
while j < bllen and b[j] == '0':
    j += 1
alen = allen - i
blen = bllen - j
m = min(alen, blen)

def func_1(a, b, i, j):
    if alen > blen:
        return '>'
    elif alen < blen:
        return '<'
    while i < allen and j < bllen:
        if a[i] < b[j]:
            return '<'
        elif a[i] > b[j]:
            return '>'
        i += 1
        j += 1
    return '='
print(func_1(a, b, i, j))