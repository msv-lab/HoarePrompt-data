#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. Each test case consists of two lines: the first line contains a single integer n such that 2 ≤ n ≤ 10^5, and the second line contains n integers a_1, a_2, …, a_n such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: Output State: `t` is exactly 3, `n` is greater than or equal to 3, `a` is a list of integers converted from input, `max` is the maximum of the second smallest values (i.e., the second element) of all possible sublists of three consecutive elements in the list `a`, `temp` is a sublist of `a` containing the last three elements of `a` which are sorted, `i` is `n-2`.
    #
    #In this final state, `t` will be exactly 3 since the loop runs `t` times, and `t` is initialized to 3. `n` remains the same as it was provided as input and not modified within the loop. The list `a` remains intact but is processed through the loop. The variable `max` will hold the highest value among the second smallest values of all possible sublists of three consecutive elements in the list `a`. The variable `temp` will contain the last three elements of `a` after the loop has completed, and these elements will be sorted. The variable `i` will be `n-2` because the loop runs from `range(n-2)`.
#Overall this is what the function does:Functionality: The function processes a series of test cases, where each test case consists of an integer \( n \) (with \( 2 \leq n \leq 10^5 \)) followed by \( n \) integers \( a_1, a_2, \ldots, a_n \) (each between 1 and \( 10^9 \)). For each test case, the function finds the maximum value among the second smallest elements of all possible sublists of three consecutive elements in the list \( a \), and prints this value. If \( n \) is 2, it simply prints the minimum of the two elements.

