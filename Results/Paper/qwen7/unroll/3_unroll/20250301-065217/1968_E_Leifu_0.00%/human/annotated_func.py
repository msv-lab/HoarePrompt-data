#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
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
        
    #State: Output State: t lines of output where each line contains '1 1', '1 2', and then either '2 3' or '2 4' followed by a sequence of numbers from 4 to the input value n (inclusive). Each line corresponds to one iteration of the loop with the value of n being the input for that iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( t \) and \( n \), where \( 1 \leq t \leq 50 \) and \( 2 \leq n \leq 10^3 \). For each test case, it prints a specific sequence of numbers. Specifically, it prints "1 1", "1 2", followed by either "2 3" or "2 4" depending on whether \( n \) is 3 or not. If \( n \) is greater than 3, it also prints numbers from 4 to \( n \) inclusive. After processing all test cases, it outputs \( t \) lines of these sequences, corresponding to each test case.

