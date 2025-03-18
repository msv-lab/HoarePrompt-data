#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: For each test case, the output consists of the lines `1 1`, `1 2`. If `n` is 3, it includes `2 3`. If `n` is greater than 3, it includes `2 4` followed by `j j` for `j` from 4 to `n`.
#Overall this is what the function does:The function processes `t` test cases, where each test case involves an integer `n`. For each test case, it outputs specific pairs of numbers based on the value of `n`. It always outputs `1 1` and `1 2`. If `n` is 3, it outputs `2 3`. If `n` is greater than 3, it outputs `2 4` followed by `j j` for each `j` from 4 to `n`.

