#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` and an integer `n` representing the length of the list `a`. The list `a` is a beautiful array as defined in the problem, and `1 <= n <= 3 * 10^5`. Additionally, the function should be able to handle multiple test cases, where the number of test cases `t` satisfies `1 <= t <= 10^4` and the sum of `n` over all test cases does not exceed `3 * 10^5`.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: The list `a` remains unchanged, `n` remains the same input integer, `arr` remains the same list of integers, and `flag` is `False` if any two consecutive elements in `arr` are different, otherwise `flag` remains `True`.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `a` remains unchanged, `n` remains the same input integer, `arr` remains the same list of integers, `flag` is `False` if any two consecutive elements in `arr` are different, otherwise `flag` remains `True`, `ans` is the minimum count of consecutive elements equal to `val` (or `Decimal('Infinity')` if no such sequence exists), `val` is set to the first element of `arr`, `cnt` is the count of the last sequence of consecutive elements equal to `val`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum count of consecutive elements equal to the first element of `arr`, or `Decimal('Infinity')` if no such sequence exists)
    #State: *`a` remains unchanged, `n` remains the same input integer, `arr` remains the same list of integers, `val` is set to the first element of `arr`, `cnt` is the count of the last sequence of consecutive elements equal to `val`. If `flag` is `True`, all consecutive elements in `arr` are the same, and `ans` is the minimum count of consecutive elements equal to `val` (or `Decimal('Infinity')` if no such sequence exists). If `flag` is `False`, at least one pair of consecutive elements in `arr` are different, and `ans` is the minimum count of consecutive elements equal to `val` (or `Decimal('Infinity')` if no such sequence exists).
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `arr` from the input for each test case. It checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it finds the minimum length of consecutive sequences of the first element in `arr` and prints this minimum length. The function handles multiple test cases, where the number of test cases `t` is implicitly managed by the calling context. The function does not modify the input list `arr` or the integer `n`.

