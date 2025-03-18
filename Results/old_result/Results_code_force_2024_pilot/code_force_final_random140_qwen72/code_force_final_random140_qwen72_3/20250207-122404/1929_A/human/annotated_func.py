#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, and a is a list of n integers where 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(sorted(list(map(int, input().split()))))
        
        print(sum([(ar[i] - ar[i - 1]) for i in range(1, n)]))
        
    #State: The loop has completed all its iterations as determined by the initial input value `t`. The variable `_` is a placeholder and does not retain any specific value. For each of the `t` test cases, `n` was an integer where 2 ≤ n ≤ 100, and `a` was a list of `n` integers where 1 ≤ a_i ≤ 10^9. After sorting, `ar` was a sorted list of `n` integers where 1 ≤ ar_i ≤ 10^9. The loop printed the sum of the differences between consecutive elements in `ar` for each test case.
#Overall this is what the function does:The function reads multiple test cases from standard input. Each test case consists of an integer `n` followed by a list of `n` integers. For each test case, the function sorts the list of integers and prints the sum of the differences between consecutive elements in the sorted list. The function does not return any value; it only prints the results to standard output. After processing all test cases, the function completes its execution.

