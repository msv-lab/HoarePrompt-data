""" ***E-property of Saket Saumya ***
            IIITM

"""
MOD = 10 ** 9 + 7
INF = float('+inf')

def func_1():
    return str(stdin.readline())

def func_2():
    return int(raw_input())

def func_3():
    return map(int, raw_input().split())

def func_4():
    return [int(i) for i in raw_input().split()]

def func_5(x):
    return stdout.write(str(x))

def func_6(list):
    return eval('*'.join((str(item) for item in list)))
'-----------------------------------------------'

def func_7(n):
    for i in range(2, int(n ** 0.5 + 100)):
        if n % i == 0 and n != i:
            return False
    return True
n = int(input())
if func_7(n):
    print(1)
elif n % 2 == 0:
    print(2)
elif func_7(n - 2):
    print(2)
else:
    print(3)