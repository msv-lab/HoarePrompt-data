#State of the program right berfore the function call: The function `func` takes no input arguments but operates on multiple test cases provided through standard input. Each test case consists of two integers, x and y, where 0 ≤ x, y ≤ 99, representing the number of 1x1 and 2x2 application icons, respectively. The first line of input contains an integer t (1 ≤ t ≤ 10^4), which denotes the number of test cases that follow.
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
        
    #State: The output state is the sequence of `t` values printed for each of the `n` test cases.
#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case consists of two integers representing the number of 1x1 and 2x2 application icons. For each test case, it calculates and prints the minimum number of 15x15 grids required to cover all the icons.

