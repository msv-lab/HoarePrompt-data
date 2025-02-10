#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and the second line of each test case contains n integers a_1, a_2, ..., a_n where 1 <= a_i <= 10^9.
def func():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: Output State: `t` must be greater than 0, `i` is equal to `t-1`, `n` is an input integer, `ls` is a list of strings from the input excluding the last element for each iteration, `last` is the integer value of the last element of the original `ls` for the last iteration, `other` is the second largest element in the sorted list of `ls` for the last iteration.
    #
    #In simpler terms, after all iterations of the loop have finished:
    #- The variable `t` will still hold its initial value as long as it was greater than 0.
    #- The loop counter `i` will be equal to `t - 1`.
    #- The variable `n` will be an integer input for the last iteration of the loop.
    #- The list `ls` will be a list of strings from the inputs excluding the last element for each iteration.
    #- The variable `last` will be the integer value of the last element of the original `ls` from the last iteration.
    #- The variable `other` will be the second largest element in the sorted list of `ls` from the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer \( t \) indicating the number of sub-cases. For each sub-case, it reads an integer \( n \) and a list of \( n \) integers. It then calculates and prints the sum of the largest and second-largest integers from the list for each sub-case. After processing all sub-cases, the function does not return any value but prints the results for each sub-case.

