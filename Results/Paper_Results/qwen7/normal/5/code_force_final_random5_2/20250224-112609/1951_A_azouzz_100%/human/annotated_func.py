#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end are used to filter folder names which should be digits within the specified range.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2:
            print('NO')
        elif cnt1 == 1:
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: After all iterations of the loop have finished, `t` will be 0, `n` will be an input integer for the last iteration, `s` will be the string input for the last iteration, and `cnt1` will be the number of '1's in `s` for the last iteration.
#Overall this is what the function does:The function reads multiple test cases. For each test case, it takes an integer `n` and a string `s`. It then checks the number of '1's in the string `s`. Based on the count of '1's and their arrangement, it prints either 'YES' or 'NO'. Specifically, if the count of '1's is greater than 2 and even, it prints 'YES'; if the count is greater than 2 but odd, or if there are exactly two consecutive '1's, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function ends.

