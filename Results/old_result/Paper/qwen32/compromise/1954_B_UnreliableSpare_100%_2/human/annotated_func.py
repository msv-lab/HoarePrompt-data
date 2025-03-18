#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5. The array a is guaranteed to be beautiful according to the problem's definition.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: - `t` remains the same.
    #- `n` remains the same.
    #- `a` remains the same.
    #- `arr` remains the same.
    #- `flag` will be `True` if all elements in `arr` are the same; otherwise, it will be `False`.
    #
    #Output State:
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `t` remains the same; `n` remains the same; `a` remains the same; `arr` remains the same; `flag` will be `True` if all elements in `arr` are the same; otherwise, it will be `False`; `ans` is the length of the shortest sequence of consecutive elements that are equal to `val` found in `arr`, or `Decimal('Infinity')` if all elements are the same; `val` remains the same; `cnt` is the count of the final sequence of consecutive elements that are equal to `val`.
    #
    #Output State:
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum of its previous value and cnt, and cnt is the count of the final sequence of consecutive elements in arr that are equal to val)
    #State: `t`, `n`, `a`, `arr`, `val`, and `cnt` remain the same. `flag` is `True` if all elements in `arr` are the same, otherwise `flag` is `False`. `ans` is the minimum of its current value and `cnt`.
#Overall this is what the function does:The function reads an integer `n` and a list `arr` of `n` integers. It checks if all elements in `arr` are the same. If they are, it outputs `-1`. Otherwise, it outputs the length of the shortest sequence of consecutive elements that are equal in `arr`.

