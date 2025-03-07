def func_1(s):
    cost = 0
    one = 0
    for i in s:
        if i == '1':
            one += 1
        elif i == '0' and one > 0:
            cost += one + 1
    return cost
t = int(input())
while t:
    s = input()
    print(func_1(s))
    t = t - 1