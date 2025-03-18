#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each of the t test cases, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n over all test cases does not exceed 3 * 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: t is an integer such that 1 <= t <= 10^4; n is the integer input value; a is a list of n integers where 1 <= a_i <= n; arr is a list of integers derived from the input; flag is True if all elements in arr are the same; otherwise, flag is False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer input value and must be greater than or equal to 1; `a` is a list of `n` integers where 1 <= a_i <= n; `arr` is a list of integers derived from the input; `flag` is True if all elements in `arr` are the same; otherwise, `flag` is False; `ans` is the minimum length of sequences of consecutive elements equal to `val` found during the loop, or `Decimal('Infinity')` if all elements are the same; `val` is `arr[0]`; `cnt` is the length of the last sequence of consecutive elements equal to `val`; `i` is `n`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: - The `print` statement will output `-1`.
        #
        #Output:
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum length of consecutive elements in arr that are equal to arr[0])
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer input value and must be greater than or equal to 1; `a` is a list of `n` integers where 1 <= a_i <= n; `arr` is a list of integers derived from the input; `flag` is a boolean indicating whether all elements in `arr` are the same; `ans` is the minimum of its previous value and `cnt`; `val` is `arr[0]`; `cnt` is the length of the last sequence of consecutive elements equal to `val`; `i` is `n`.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `arr` of `n` integers. It checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it finds and prints the minimum length of consecutive elements in `arr` that are equal to the first element of `arr`.

