#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, x and y are integers such that 0 ≤ x, y ≤ 99, and ap is an input integer.
#Overall this is what the function does:The function `func_1` processes `t` test cases, where each test case consists of two integers `x` and `y` such that 0 ≤ x, y ≤ 99. For each test case, it calculates and prints a value based on the given conditions: the sum of the ceiling of `y/2` and the ceiling of the adjusted `x` value divided by 15, or simpler values depending on whether `x` or `y` is zero.

