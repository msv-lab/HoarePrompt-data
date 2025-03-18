#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, representing the length of the array a. The array a consists of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(sorted(list(map(int, input().split()))))
        
        print(sum([(ar[i] - ar[i - 1]) for i in range(1, n)]))
        
    #State: `t` is an integer where 1 ≤ t ≤ 500, `_` is `t-1`, `n` is an input integer greater than 0, `ar` is a sorted list of integers input by the user.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves reading an integer `n` and a list of `n` integers. It sorts the list and then calculates the sum of the differences between consecutive elements in the sorted list. This sum is printed for each test case. After processing all test cases, the function completes without returning any value. The final state of the program is that the input has been processed and the results have been printed for each test case.

