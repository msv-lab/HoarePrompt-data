input = lambda : sys.stdin.readline().rstrip()

def func_1():
    return list(map(int, input().split()))

def func_2():
    return map(int, input().split())

def func_3():
    a = int(input())
    b = input()
    c = input()
    first = 0
    second = 0
    for i in range(a):
        if int(b[i]) > int(c[i]):
            first += 1
        elif int(b[i]) < int(c[i]):
            second += 1
    if first > second:
        print('RED')
    elif second > first:
        print('BLUE')
    else:
        print('EQUAL')

def func_4():
    for _ in range(int(input())):
        func_3()
if __name__ == '__main__':
    func_4()