#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` and an integer `n` representing the length of the list `a`. The list `a` is a beautiful array where 1 ≤ n ≤ 3 · 10^5 and 1 ≤ a_i ≤ n. The array `a` is guaranteed to be beautiful according to the problem's definition. The function should also handle multiple test cases, indicated by an integer `t` where 1 ≤ t ≤ 10^4. The sum of `n` over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `n` remains unchanged, `i` is `n-1`, and `flag` is False if any two consecutive elements in `arr` are not equal, otherwise `flag` remains True.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: `n` remains unchanged, `i` is `n-1`, `flag` is False if any two consecutive elements in `arr` are not equal, otherwise `flag` remains True, `val` is `arr[0]`, `cnt` is the number of times `arr[0]` appears in `arr`, and `ans` is the minimum number of consecutive occurrences of `arr[0]` before a different element is encountered. If `arr[0]` never changes throughout the array, `ans` remains Decimal('Infinity').
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: - The `print(ans)` statement will print the value of `ans`, which is the minimum of the initial `ans` and the count of `arr[0]` in the list `arr`.
        #
        #Output:
    #State: *`n` remains unchanged, `i` is `n-1`, `val` is `arr[0]`, `cnt` is the number of times `arr[0]` appears in `arr`, and `ans` is the minimum of the initial `ans` and `cnt`. If `arr[0]` never changes throughout the array, `ans` remains Decimal('Infinity'). If `flag` is True, it indicates that all consecutive elements in `arr` are equal. If `flag` is False, it indicates that there are at least two consecutive elements in `arr` that are not equal.
#Overall this is what the function does:The function `func_1` processes a list of integers `arr` of length `n` for each of `t` test cases. It checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it finds the minimum number of consecutive occurrences of the first element in `arr` and prints this value. The function does not return any value but prints the result directly. After the function concludes, `n` remains unchanged, `arr` is the original list of integers, and the state of the program is as it was before the function call, except for the printed output.

