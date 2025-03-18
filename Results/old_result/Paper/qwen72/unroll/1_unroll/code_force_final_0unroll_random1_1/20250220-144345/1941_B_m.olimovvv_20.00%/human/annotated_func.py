#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_j is such that 0 <= a_j <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: The loop has finished executing all iterations, and the values of `t`, `n`, and the list `a` remain unchanged. The loop has printed 'YES' or 'NO' for each iteration based on the conditions checked within the loop.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then checks if the first and second elements of `a` or the last and second-to-last elements of `a` meet specific conditions. If the conditions are not met, it prints 'NO'; otherwise, it prints 'YES'. The function does not modify the values of `t`, `n`, or the list `a`. After processing all test cases, the function concludes, and the state of the program remains unchanged except for the printed output.

