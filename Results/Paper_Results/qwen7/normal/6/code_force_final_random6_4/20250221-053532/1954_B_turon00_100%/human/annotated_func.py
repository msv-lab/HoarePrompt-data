#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. Additionally, the sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        if n == 1 or ans == n:
            print(-1)
        else:
            print(ans)
        
    #State: Output State: After all iterations of the loop have finished, `t` will be 0, `i` will be `3 * n`, `tmp` will be equal to the first element of the list `a`, `ans` will hold the minimum count of consecutive occurrences of `tmp` found during the loop's execution across all inputs, `n` will remain unchanged for each individual input but will be processed sequentially, and either `n == 1 or ans == n` is satisfied for each input, or `i` will be greater than or equal to the length of the list `a` for each input.
    #
    #This means that after processing all `t` inputs, the counter `t` will have been decremented to 0, and for each input, the loop will have fully processed the list `a` up to `3 * n` (considering the summation effect of incrementing `i` by `n` for each input), with `tmp` holding the first element of the list for the current input, `ans` containing the minimum count of consecutive occurrences of `tmp` for that input, and the conditions for printing `-1` or the result will have been evaluated and printed as necessary.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `n`, an integer `t`, and an array `a` of `n` integers. For each test case, it finds the minimum count of consecutive occurrences of the first element in the array `a`. If the array has only one element or the minimum count is equal to `n`, it prints `-1`; otherwise, it prints the minimum count. After processing all test cases, it ensures that `t` is decremented to 0 and all other variables are in their expected final states.

