#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, representing the number of test cases. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, representing the size of the array, and a is a list of n integers such that 1 <= a_i <= n, representing the elements of the array. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        le = len(a)
        
        l, r = 0, n - 1
        
        st, end = 1, 1
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        ans = le - max(st, end)
        
        if a[0] == a[-1]:
            ans = max(0, le - (st + end))
        
        print(ans)
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an input integer greater than 1, `a` is a list of integers provided by the new input for each test case, `le` is the length of the list `a`, `l` is the index of the first element in `a` that is not equal to `a[0]` or `n - 1` if all elements are equal, `r` is the index of the last element in `a` that is not equal to `a[-1]` or `0` if all elements are equal, `st` is the number of consecutive elements from the start of the list `a` that are equal to `a[0]`, `end` is the number of consecutive elements from the end of the list `a` that are equal to `a[-1]`, `ans` is `le - max(st, end)` if `a[0] != a[-1]` or `max(0, le - (st + end))` if `a[0] == a[-1]`.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` representing the size of an array and a list `a` of `n` integers. For each test case, it calculates the number of elements in the array that need to be removed to make the array either empty or have all elements equal to the first or last element, depending on the specific conditions. The function prints the result for each test case. After the function concludes, `t` is an integer such that 1 <= t <= 10^4, `n` is an input integer greater than 1, `a` is a list of integers provided by the new input for each test case, `le` is the length of the list `a`, `l` is the index of the first element in `a` that is not equal to `a[0]` or `n - 1` if all elements are equal, `r` is the index of the last element in `a` that is not equal to `a[-1]` or `0` if all elements are equal, `st` is the number of consecutive elements from the start of the list `a` that are equal to `a[0]`, `end` is the number of consecutive elements from the end of the list `a` that are equal to `a[-1]`, and `ans` is `le - max(st, end)` if `a[0] != a[-1]` or `max(0, le - (st + end))` if `a[0] == a[-1]`.

