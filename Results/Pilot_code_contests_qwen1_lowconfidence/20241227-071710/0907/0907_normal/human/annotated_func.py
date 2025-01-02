#State of the program right berfore the function call: The input is a list of integers representing the parameter t for each customer, where the length of the list is n (1 ≤ n ≤ 10^5) and each element ti satisfies -10 ≤ ti ≤ 10.
def func():
    a = dict()
    for i in range(-10, 11):
        a[i] = 0
        
    #State of the program after the  for loop has been executed: `i` is in the range from -10 to 10, inclusive; for every integer `k` in this range, `a[k]` is 0.
    n = input()
    t = map(int, raw_input().split())
    for i in range(n):
        a[t[i]] += 1
        
    #State of the program after the  for loop has been executed: `i` is in the range from -10 to 10, `n` is the length of the list `n`, `a[t[i]]` is the count of each element in the list `t` that falls within the range from -10 to 10.
    ans = 0
    for i in range(-10, 0):
        ans += a[i] * a[-i]
        
    #State of the program after the  for loop has been executed: `i` is -10, `n` is the length of the list `t`, `a[t[i]]` is the count of each element in the list `t` that falls within the range from -10 to 10, `ans` is the sum of `a[i] * a[-i]` for all `i` in the range from -10 to 0.
    ans += a[0] * (a[0] - 1) / 2
    print(ans)
#Overall this is what the function does:The function `func` accepts a list of integers representing the parameter `t` for each customer. It checks if all values in the list fall within the range `-10 ≤ ti ≤ 10`. If any value is outside this range, the function raises an error. If all values are within the specified range, the function calculates a specific output based on the counts of pairs of integers that are additive inverses (i.e., if `a` is in the list, then `-a` is also counted towards the result). The final output is the sum of the products of the counts of these pairs plus the adjusted count for zero (if it appears in the list). If zero appears more than once, the adjusted count considers combinations of zero pairs.

