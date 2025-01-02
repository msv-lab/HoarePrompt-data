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
            
        #State of the program after the  for loop has been executed: `n` is an integer input between 1 and 500,000, `a` is a list of `n` integers where each integer is between \(-10^9\) and \(10^9\) (inclusive), `neg` is 0, `pos` is `n`, `ans` is the maximum value between its original value and either `s - a[i - 1]` if `i > 0` and `a[i] < a[i - 1]` or `s - a[i + 1]` if `i < n - 1` and `a[i] < a[i + 1]` for all valid `i`, `s` is the sum of all elements in list `a`.
        print(ans)
    #State of the program after the if-else block has been executed: `n` is an integer input between 1 and 500,000, `a` is a list of `n` integers where each integer is between \(-10^9\) and \(10^9\) (inclusive), `neg` is the number of negative integers in list `a`, `pos` is `n - neg`. If `neg` is greater than 0, the sum of the absolute values of all elements in list `a` is printed. Otherwise, `ans` is the maximum value between its original value and either `s - a[i - 1]` if `i > 0` and `a[i] < a[i - 1]` or `s - a[i + 1]` if `i < n - 1` and `a[i] < a[i + 1]` for all valid `i`, where `s` is the sum of all elements in list `a`, and `ans` is printed.
#Overall this is what the function does:The function processes a list of integers `a` and calculates a specific value based on the contents of the list. If the list contains any negative numbers, the function prints the sum of the absolute values of all elements in the list. Otherwise, it iterates through the list to find the maximum subarray sum where the sum is calculated as the total sum of the list minus a specific element, considering the condition that the current element is less than its adjacent elements. The function then prints the maximum value found. The function ensures that the input list `a` meets the constraints of having a length between 1 and 500,000 and each element being between \(-10^9\) and \(10^9\). If these constraints are violated, the function does not execute properly.

