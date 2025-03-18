#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func():
    t = int(input())
    for tc in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        maxsize = max(a)
        
        a.sort()
        
        mexsize = 1
        
        for sz in a:
            if sz == mexsize:
                mexsize = mexsize + 1
        
        if mexsize > maxsize:
            print('Alice' if mexsize % 2 == 0 else 'Bob')
        else:
            print('Alice' if mexsize % 2 == 1 else 'Bob')
        
    #State: Output State: The output state will consist of a series of strings printed based on the conditions inside the loop. For each iteration of the loop (from `tc` in `range(t)`), the program reads an integer `n`, followed by a list of integers `a`. It then calculates the maximum value (`maxsize`) in the list `a`, sorts the list, and finds the smallest missing positive integer (`mexsize`). Depending on the comparison between `mexsize` and `maxsize`, it prints either "Alice" or "Bob" with a condition based on whether `mexsize` is even or odd. The output state will be a sequence of these printed strings, one for each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` representing the number of test cases, followed by `t` pairs of integers `n` and a list of `n` integers `a`. It calculates the maximum value in the list `a`, sorts the list, and determines the smallest missing positive integer. Based on the comparison between this smallest missing positive integer and the maximum value in the list, it prints either "Alice" or "Bob" with a condition based on whether the smallest missing positive integer is even or odd. The function does not return any value but outputs a sequence of strings "Alice" or "Bob" for each test case.

