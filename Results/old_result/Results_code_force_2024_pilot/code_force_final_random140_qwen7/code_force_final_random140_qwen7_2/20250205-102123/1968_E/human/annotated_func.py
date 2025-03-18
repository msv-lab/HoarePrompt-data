#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        elif n >= 4:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: t must be greater than 0 and less than or equal to 50, i is 3, and either j is 16 and n is greater than or equal to 4, or j remains 13 and n is 3.
#Overall this is what the function does:The function processes multiple test cases defined by `t`. For each test case, it reads an integer `n` and prints specific pairs of numbers based on the value of `n`. If `n` is 3, it prints "2 3". If `n` is 4 or greater, it prints "2 4" followed by pairs of numbers from 4 to `n`. After processing all test cases, the function does not return any value.

