#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the given array a is beautiful. The sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: `flag` remains False, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` must be greater than or equal to the value of `i` which will be `n-1` after the loop completes, `a` is a list of `n` integers where \(1 \leq a_i \leq n\), and `i` is `n-1`. The condition `arr[i] != arr[i - 1]` was found to be true at some point during the loop's execution, causing `flag` to be set to `False` and breaking out of the loop.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: Output State: `flag` remains `False`, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` must be greater than or equal to the final value of `i` after the loop completes, `a` is a list of `n` integers where \(1 \leq a_i \leq n\), and `i` is `-1` (since the loop runs from `0` to `n-1` and then `i` becomes `-1`). `cnt` is the maximum count of consecutive elements in `a` that are equal to `val` found during the loop, and `ans` is the minimum value of `cnt` encountered when `arr[i]` is not equal to `val`. `val` is the last element of the list `a` that was checked in the loop.
    #
    #In simpler terms, after the loop completes, `ans` will hold the length of the longest sequence of consecutive elements in the list `a` that are different from `val`. The variable `cnt` will reflect the current count of consecutive elements equal to `val`, and `val` will be the last element of the list `a` that was compared against `val` in the loop.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum value between its initial value and the maximum count of consecutive equal elements found in the list a)
#Overall this is what the function does:The function processes an array of integers `a` for multiple test cases. For each test case, it first checks if the array is "beautiful" (i.e., all elements are the same). If the array is not beautiful, it finds the length of the longest sequence of consecutive elements that are different from the most frequent element in the array. If the array is beautiful, it prints `-1`; otherwise, it prints the length of the longest sequence of non-matching consecutive elements.

