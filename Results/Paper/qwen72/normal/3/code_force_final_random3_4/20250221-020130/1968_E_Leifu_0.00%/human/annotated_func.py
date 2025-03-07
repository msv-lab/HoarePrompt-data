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
        
    #State: t is an integer input by the user such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3. The loop has finished executing, and the values of t and n remain unchanged. The loop has printed '1 1', '1 2', and depending on the value of n, either '2 3' if n == 3, or '2 4' followed by pairs of integers (j, j) for j ranging from 4 to n.
#Overall this is what the function does:The function `func` processes a series of test cases, where the number of test cases `t` is an integer between 1 and 50. For each test case, it reads an integer `n` between 2 and 10^3. The function prints the pairs '1 1' and '1 2'. If `n` is 3, it prints '2 3'. Otherwise, it prints '2 4' followed by pairs of integers (j, j) for each `j` ranging from 4 to `n`. The function does not return any value, and the values of `t` and `n` remain unchanged after the function execution.

