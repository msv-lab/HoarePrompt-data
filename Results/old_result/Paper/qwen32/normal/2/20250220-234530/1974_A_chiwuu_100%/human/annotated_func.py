#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, there are two integers x and y such that 0 ≤ x, y ≤ 99.
def func():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b
        
        if t % 2 == 0:
            t = t // 2
        else:
            t = t // 2 + 1
        
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
        
    #State: The final value of `t` after `n` iterations, where `t` is updated according to the rules specified in the loop for each pair of `a` and `b` read from the input.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then calculates and prints a value `t` based on the given conditions for each pair of `a` and `b`.

