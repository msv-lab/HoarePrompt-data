num = int(input())

def func_1(a, num2):
    order = 0
    for i in range(1, num2):
        if a[i - 1] >= a[i]:
            order += 1
    if order == 0:
        return True
    else:
        return False
for i in range(0, num):
    num2 = int(input())
    case = input()
    a = [int(i) for i in case.split() if i.isdigit()]
    if func_1(a, num2):
        print(0)
    else:
        beauty = 0
        b = sorted(a)
        for x in range(1, num2):
            beauty += b[x] - b[x - 1]
        print(beauty)