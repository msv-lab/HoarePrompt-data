#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, a and b are integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for i in range(t):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
        if (a + b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is the integer input provided, and 1 <= `t` <= 1000; the loop has executed `t` times; `i` is equal to `t` after the loop has finished; for each iteration `i` from 0 to `t-1`, the string `s` was provided, `a` was the integer value of the first substring of `s`, `b` was the integer value of the second substring of `s`, and the program printed 'Bob' if `a + b` was even, otherwise it printed 'Alice'.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`, and prints 'Bob' if the sum of `a` and `b` is even, otherwise it prints 'Alice'.

