#State of the program right berfore the function call: The function should take two parameters, x and y, where x and y are integers such that 0 <= x, y <= 99.
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
        
    #State: `x` and `y` are integers such that 0 <= x, y <= 99; `n` is an input integer; `i` is `n - 1`; `a` is the integer value of the last input string's first part; `b` is the integer value of the last input string's second part; `t` is calculated based on the last input values of `a` and `b` as follows: `t` is either `b * 2 // 5` or `b * 2 // 5 + 1` depending on whether `b * 2` is divisible by 5. If `t1` (which is `t * 15 - b * 4`) is greater than or equal to `a`, then `t1` remains `t * 15 - b * 4` and is greater than or equal to `a`. Otherwise, `t2` is `a - t1`, and `t` is updated to `t + t2 // 15` (or `t + t2 // 15 + 1` if `t2 % 15 != 0`).
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer `n` from the user input, which represents the number of pairs of integers to process. For each of the `n` pairs, it reads two integers `a` and `b`, calculates a value `t` based on these integers, and prints the result. The value of `t` is determined by a series of arithmetic and conditional operations involving `a` and `b`. After processing all pairs, the function concludes without modifying any external state.

