def func_1(isOne=False):
    if not isOne:
        return int(input())
    else:
        return 1

def func_2(space=True, to_int=True):
    line = input()
    if space:
        items = line.split()
    else:
        items = list(line)
    if to_int:
        return [int(i) for i in items]
    else:
        return items

def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
    return string

def func_4(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        index = string.find(substring, index + 1)
    return indices

def func_5(arr, element):
    return [index for (index, value) in enumerate(arr) if value == element]

def func_6(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
    return None

def func_7():
    n = int(input())
    start = -1
    end = int(1000000000.0)
    num = []
    for i in range(n):
        (t, v) = tuple(map(int, input().split()))
        if t == 1:
            if start < v:
                start = v
        if t == 2:
            if end > v:
                end = v
        if t == 3:
            num.append(v)
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
    return end - start + 1 - count_num if start <= end else 0
n = func_1()
ans = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    ans.append(func_7())
for i in ans:
    print(i)