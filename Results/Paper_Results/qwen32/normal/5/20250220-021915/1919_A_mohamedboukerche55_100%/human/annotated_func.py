#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a and b are integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 1000; all t test cases have been processed; for each test case, the program has read a string `s`, split it to get integers `a` and `b`, and printed 'Bob' if (a + b) is even, otherwise printed 'Alice'; i is equal to t.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `a` and `b`. For each test case, it prints 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd.

