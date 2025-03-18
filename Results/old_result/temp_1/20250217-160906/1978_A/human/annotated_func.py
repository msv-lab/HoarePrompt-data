#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 500, and for each test case, n is an integer such that 2 <= n <= 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n such that 1 <= a_i <= 10^9.
def func():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: Output State: The value of `t` remains unchanged, but for each iteration `i` from 0 to `t-1`, the output is the sum of the last element and the second largest element of the list `ls`. The final state includes the value of `t` and the cumulative effect of all printed values.
#Overall this is what the function does:The function processes multiple test cases, each containing a positive integer `n` and a list of `n` integers. For each test case, it finds the last element and the second largest element in the list, calculates their sum, and prints the result. After processing all test cases, it outputs the cumulative effect of these sums. The function does not return any value but modifies the console output based on the input data.

