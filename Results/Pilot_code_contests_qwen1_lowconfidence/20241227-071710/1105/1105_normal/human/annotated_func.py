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
            
        #State of the program after the  for loop has been executed: `i` is `n - 1`, `n` is an integer such that \(1 \leq n \leq 500,000\), `a` is a list of integers, and `ans` is the maximum value of `s - a[j]` for any `j` where either `a[j] < a[j - 1]` or `a[j] < a[j + 1]`.
        print(ans)
    #State of the program after the if-else block has been executed: *`n` is an integer such that \(1 \leq n \leq 500,000\); `a` is a list of `n` integers where each integer \(a_i\) satisfies \(-10^9 \leq a_i \leq 10^9\); `rints` is a lambda function defined to read and split a line of space-separated integers into a list of integers; `neg` is the count of negative numbers in `a`. If `neg` is greater than 0, the absolute values of all elements in `a` are summed up and printed. Otherwise, the maximum value of `s - a[j]` for any `j` where either `a[j] < a[j - 1]` or `a[j] < a[j + 1]` is found and printed.
#Overall this is what the function does:The function processes a list of integers `a` and calculates a specific result based on the content of the list. If the list contains at least one negative number, the function prints the sum of the absolute values of all elements in the list. If the list does not contain any negative numbers, the function iterates through the list and finds the maximum value of `s - a[j]` for any `j` where `a[j] < a[j - 1]` or `a[j] < a[j + 1]`, where `s` is the sum of all elements in the list. The function then prints the maximum value found. The function does not return any value, but it prints the calculated result. Potential edge cases include an empty list or a list with only non-negative numbers. In these cases, the function will still correctly compute and print the result based on the given conditions.

