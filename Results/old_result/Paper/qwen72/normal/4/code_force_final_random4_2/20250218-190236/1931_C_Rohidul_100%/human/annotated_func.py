#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the elements of the array for each test case. The length of each inner list n (1 ≤ n ≤ 2 · 10^5) is the size of the array. The sum of n for all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has executed `t` times, where `t` is the number of test cases provided initially. For each test case, the variables `n`, `a`, `le`, `l`, `r`, `st`, `end`, and `ans` have been updated according to the logic of the loop. Specifically, for each test case, `n` is the length of the list `a`, `a` is the list of integers provided by the user, `le` is the length of `a`, `l` is the index of the first element in `a` that is not equal to the next element, `r` is the index of the last element in `a` that is not equal to the previous element, `st` is the number of consecutive equal elements from the start of the list `a`, `end` is the number of consecutive equal elements from the end of the list `a`, and `ans` is the result of the computation `le - max(st, end)` unless the first and last elements of `a` are equal, in which case `ans` is `max(0, le - (st + end))`. The final output for each test case is the value of `ans`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of integers `a` from the input. It then calculates the number of consecutive equal elements from the start (`st`) and the end (`end`) of the list `a`. The function computes the result `ans` as the length of the list `a` minus the maximum of `st` and `end`. If the first and last elements of `a` are equal, `ans` is adjusted to be the length of the list minus the sum of `st` and `end`, ensuring `ans` is non-negative. The function prints the result `ans` for each test case. After processing all test cases, the function completes without returning any value.

