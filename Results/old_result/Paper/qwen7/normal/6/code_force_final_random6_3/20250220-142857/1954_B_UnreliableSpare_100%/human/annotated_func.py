#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5; the array a is a list of n integers such that 1 ≤ a_i ≤ n, and the array a is beautiful; the sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: `flag` is `False`, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` must be greater than 1, `i` is equal to `n-1`, and if `arr[i]` is not equal to `arr[i - 1]`, we break out of the most internal loop or if statement.
    #
    #Explanation: After the loop completes all its iterations, the value of `i` will be `n-1` because the loop runs from `1` to `n-1`. The variable `flag` is set to `False` as soon as any two consecutive elements in the array `arr` are found to be different, causing the loop to break. Since the loop breaks on the first difference encountered, `flag` remains `False` regardless of how many iterations it takes to find the difference. The variable `t` and the condition on `n` (which must be greater than 1) remain unchanged as they are not affected by the loop.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `flag` is `False`, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is greater than 1, `i` is `0`, `ans` is the minimum count of consecutive occurrences of `val` in `arr`, and `cnt` is `0`
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: 0
    #State: `flag` is either `True` or `False`, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is greater than 1, `i` is `0`, `ans` is the minimum count of consecutive occurrences of `val` in `arr` after updating it with `min(ans, cnt)`, and `cnt` is `0`.
#Overall this is what the function does:The function processes a single test case consisting of an integer `n`, an array `arr` of length `n`, and implicitly an integer `t`. It checks if the array `arr` is monotonically the same (i.e., all elements are identical). If the array is not monotonically the same, it calculates the minimum number of consecutive identical elements in the array. Finally, it prints `-1` if the array is monotonically the same, otherwise it prints the calculated minimum count.

