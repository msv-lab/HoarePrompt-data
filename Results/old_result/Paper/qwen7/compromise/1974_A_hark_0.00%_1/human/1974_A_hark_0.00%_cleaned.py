def func_1(a, b):
    return a if a < b else b

def func_2():
    (x, y) = map(int, input().split())
    if x > 0 and y > 0:
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
    elif x == 0 and y > 0:
        print(math.ceil(y / 2))
    elif x > 0 and y == 0:
        print(math.ceil(x / 15))
    else:
        print(0)

def func_3():
    t = int(input())
    for _ in range(t):
        func_2()
if __name__ == '__main__':
    func_3()