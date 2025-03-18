#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers such that 1 <= a_i <= n. The array a is guaranteed to be beautiful. The sum of n over all test cases does not exceed 3 * 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an input integer such that 1 <= n <= 3 * 10^5; `a` is a list of `n` integers such that 1 <= a_i <= n; `arr` is a list of integers read from input; `flag` is True if all elements in `arr` are the same, otherwise `flag` is False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: t is an integer such that 1 <= t <= 10^4; n is an input integer such that 1 <= n <= 3 * 10^5; a is a list of n integers such that 1 <= a_i <= n; arr is a list of integers read from input; flag is True if all elements in arr are the same, otherwise flag is False; ans is the minimum length of consecutive identical elements in arr; val is the last unique element counted in the loop; cnt is the length of the last sequence of identical elements in arr.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum length of consecutive identical elements in arr)
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an input integer such that 1 <= n <= 3 * 10^5; `a` is a list of `n` integers such that 1 <= a_i <= n; `arr` is a list of integers read from input; `flag` is a boolean indicating whether all elements in `arr` are the same; `ans` is the minimum length of consecutive identical elements in `arr`; `val` is the last unique element counted in the loop; `cnt` is the length of the last sequence of identical elements in `arr`. If `flag` is True, all elements in `arr` are the same. If `flag` is False, not all elements in `arr` are the same. In both cases, `ans` is the minimum of its previous value and `cnt`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it determines the minimum length of consecutive identical elements in the list `a`. If all elements in `a` are the same, it outputs `-1`. Otherwise, it outputs the minimum length of consecutive identical elements.

