#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, there are two integers x and y such that 0 ≤ x, y ≤ 99.
def func_1():
    ap = int(input())
    for k in range(ap):
        x, y = map(int, input().split())
        
        if x > 0 and y > 0:
            bxsfory = math.ceil(y / 2)
            x = x - bxsfory * 15 + y * 4
            bxsfory1 = 0 if x <= 0 else math.ceil(x / 15)
            print(bxsfory1 + bxsfory)
        elif x == 0 and y > 0:
            print(math.ceil(y / 2))
        elif x > 0 and y == 0:
            print(math.ceil(x / 15))
        else:
            print(0)
        
    #State: 
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of two integers `x` and `y`. For each test case, it calculates and prints a value based on specific conditions involving `x` and `y`. If both `x` and `y` are greater than zero, it computes a combined result considering both values. If only `y` is greater than zero, it computes a result based solely on `y`. If only `x` is greater than zero, it computes a result based solely on `x`. If both `x` and `y` are zero, it prints `0`.

