#State of the program right berfore the function call: The function should accept two parameters, x and y, where x is the number of applications with a 1 \times 1 icon and y is the number of applications with a 2 \times 2 icon. Both x and y are integers such that 0 <= x, y <= 99.
def func():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b * 2
        
        if t % 5 == 0:
            t = t // 5
        else:
            t = t // 5 + 1
        
        t1 = t * 15 - b * 4
        
        if t1 >= a:
            t = t
        else:
            t2 = a - t1
            if t2 % 15 == 0:
                t = t + t2 // 15
            else:
                t = t + t2 // 15 + 1
        
        print(t)
        
    #State: The values of `x` and `y` remain unchanged, and the loop prints the value of `t` for each iteration based on the input values `a` and `b`.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads `n` pairs of integers `(a, b)` from the user, where `a` represents the number of applications with a 1 × 1 icon and `b` represents the number of applications with a 2 × 2 icon. For each pair, it calculates and prints the minimum number of 15 × 15 grid cells required to display all the icons, considering the different sizes of the icons. The function does not return any value.

