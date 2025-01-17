#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        median_index = (n - 1) // 2
        
        median = a[median_index]
        
        operations = 0
        
        for i in range(median_index, n):
            if a[i] < median + 1:
                operations += median + 1 - a[i]
        
        results.append(operations)
        
    #State of the program after the  for loop has been executed: `t` is an integer value entered by the user that satisfies \(1 \leq t \leq 10^4\), `results` is a list containing the final value of `operations` after all iterations of the loop, `operations` is the total number of increments made to it across all iterations, `n` is the integer value entered by the user that satisfies \(1 \leq n \leq 10^4\) for each iteration, `a` is a list of integers entered by the user that is sorted in ascending order for each iteration, `median_index` is \((n - 1) // 2\) for each iteration, `median` is the element at index `median_index` in the sorted list `a` for each iteration.
    print('\n'.join(map(str, results)))
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` such that \(1 \leq t \leq 10^4\), an integer `n` such that \(1 \leq n \leq 10^5\), and an array `a` of `n` integers where \(1 \leq a_i \leq 10^9\). For each test case, it sorts the array `a` and calculates the median. It then iterates through the second half of the array, counting the number of elements that are less than `median + 1`, and accumulates these differences into a variable `operations`. After processing all test cases, it prints the results, which are the accumulated `operations` values for each test case.

