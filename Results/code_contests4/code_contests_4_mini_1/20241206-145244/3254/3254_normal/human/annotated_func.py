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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 2000, `p` is a list of `n` integers where each integer `pi` satisfies |`pi`| ≤ 10^5; `N` is greater than or equal to 0; `a` is a list of absolute values of integers from raw_input(); `ans` is the total sum of min(x, y) for each index `i`, where `x` is the count of elements in `a` less than `a[i]` that come before index `i`, and `y` is the count of elements in `a` less than `a[i]` that come after index `i`.
    print(ans)
#Overall this is what the function does:The function reads an integer `N` and a list of `N` integers, calculates the count of elements before and after each element that are smaller than the current element, and sums the minimum of these counts across all elements. The result is printed as output. If `N` is 0, the function will not perform any calculations and will output 0.

