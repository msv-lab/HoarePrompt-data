#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_j is such that 0 <= a_j <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_j is such that 0 <= a_j <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5. The loop has finished executing, and for each test case, the output is either 'YES' or 'NO' based on the conditions checked in the loop.
#Overall this is what the function does:The function reads multiple test cases from the input, where each test case consists of an integer `a` and a list of integers `b`. For each test case, it checks if the first element of `b` is odd and not equal to the second element plus 2, or if the last element of `b` is odd and not equal to the second-to-last element plus 2. If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function concludes without returning any value. The state of the program remains unchanged except for the output produced.

