#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2000, and p is a list of n integers where each integer pi satisfies |pi| ≤ 10^5.
def func():
    N, a, ans = input(), map(lambda x: abs(int(x)), raw_input().split()), 0
    for i in xrange(0, N):
        x, y = 0, 0
        
        for j in xrange(0, N):
            if a[j] < a[i]:
                if j < i:
                    x += 1
                else:
                    y += 1
        
        ans += min(x, y)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 2000; `p` is a list of `n` integers; `N` is equal to `n`; `i` is `N - 1`; `x` is the count of elements in `a` with indices less than `N - 1` that are less than `a[N - 1]`; `y` is the count of elements in `a` with indices greater than or equal to `N - 1` that are less than `a[N - 1]`; `ans` is the accumulated sum of min(`x`, `y`) for each iteration of `i` from 0 to `N - 1`.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 2000) and a list `a` of `n` integers, where each integer satisfies |ai| ≤ 10^5. It calculates the sum of the minimum counts of elements less than each element `a[i]` that are positioned before (`x`) and after (`y`) `i`. The function prints the accumulated result of these minimum counts across all elements in the list.

