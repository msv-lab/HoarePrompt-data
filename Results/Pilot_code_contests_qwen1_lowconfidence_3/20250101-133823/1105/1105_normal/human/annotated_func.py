#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 500 000, and a is a list of n integers where each integer a_i satisfies -10^9 ≤ a_i ≤ 10^9.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, a = int(input()), rints()
    neg = len(list(filter(lambda x: x < 0, a)))
    pos = n - neg
    if neg :
        print(sum(abs(x) for x in a))
    else :
        ans, s = 0, sum(a)
        for i in range(n):
            if i and a[i] < a[i - 1]:
                ans = max(ans, s - a[i - 1])
            elif i < n - 1 and a[i] < a[i + 1]:
                ans = max(ans, s - a[i + 1])
            
        #State of the program after the  for loop has been executed: `i` is equal to `n`, `n` is a non-negative integer, `a` is a list of `n` integers, `ans` is the maximum value of `ans` throughout the loop executions, considering the conditions: if `i and a[i] < a[i - 1]` is true, then `ans` is updated to `max(ans, s - a[i - 1])`; if `i < n - 1 and a[i] < a[i + 1]` is true, then `ans` is updated to `max(ans, s - a[i + 1])`. `s` is the sum of all integers in the list `a`.
        print(ans)
    #State of the program after the if-else block has been executed: `n` is the total number of integers read from input, `a` is the list of `n` integers read from input using `rints()`, `neg` is the count of negative integers in `a`, `pos` is `n - neg`. If `neg` is non-zero, the output is the sum of the absolute values of the elements in `a`. If `neg` is zero, `i` is equal to `n`, `n` is a non-negative integer, `a` is a list of `n` integers, `ans` is the maximum value of `ans` throughout the loop executions, and `ans` is printed.
#Overall this is what the function does:The function reads a list of integers from standard input, processes the list to find either the sum of the absolute values of the elements or the maximum value of a specific condition involving sums and differences of subarrays, and prints the result. Specifically, if the list contains any negative numbers, it calculates and prints the sum of the absolute values of the elements. If the list contains no negative numbers, it finds the maximum value of the sum of the list minus a single element, under certain conditions (either before or after the current element). The function accepts a list of integers and returns nothing (prints the result), handling edge cases where the input list might be empty or contain only positive numbers.

