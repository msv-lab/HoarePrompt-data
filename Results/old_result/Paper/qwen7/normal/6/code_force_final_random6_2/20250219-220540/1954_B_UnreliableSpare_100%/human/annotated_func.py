#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the given array a is beautiful. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: The loop has executed all its iterations, meaning `i` is now equal to `n-1`. The value of `n` must be greater than 1, and for each `i` from 1 to `n-1`, `arr[i]` must not be equal to `arr[i-1]`. The variable `flag` remains False throughout the entire loop execution.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `i` is `n-1`, `n` is greater than 1, `cnt` retains its final value after the last iteration, `ans` is the minimum count of consecutive occurrences of `val` found during the loop execution, and `flag` remains `False` throughout the entire loop execution.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum value between ans and cnt after the loop has completed)
#Overall this is what the function does:The function processes a list of integers `a` for multiple test cases. For each test case, it checks if the list is beautiful (i.e., all elements are the same) and finds the minimum length of consecutive identical elements. If the list is beautiful, it prints `-1`; otherwise, it prints the minimum length of consecutive identical elements.

