#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 10, representing the length of the strip. s is a string of length n, consisting of characters 'W' or 'B', where 'W' represents a white cell and 'B' represents a black cell. It is guaranteed that at least one cell in s is 'B'.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        first_black = s.find('B')
        
        last_black = s.rfind('B')
        
        min_paint = last_black - first_black + 1
        
        print(min_paint)
        
    #State: After the loop executes all the iterations, `t` is 0, `n` is the last input integer, `s` is the last input string, `first_black` is the index of the first occurrence of 'B' in the last `s` or -1 if 'B' is not found, `last_black` is the index of the last occurrence of 'B' in the last `s` or -1 if 'B' is not found, `min_paint` is `last_black - first_black + 1`.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of an integer `n` and a string `s` of length `n` containing characters 'W' or 'B'. For each test case, the function calculates the minimum number of cells that need to be painted to cover all black cells ('B') in the string `s`. This value is printed for each test case. After processing all test cases, the function completes its execution. The final state of the program includes the last processed values of `n`, `s`, `first_black`, `last_black`, and `min_paint`, but these are not returned or used outside the function.

