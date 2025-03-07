#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` and an integer `n` representing the length of the list `a`. The list `a` must be a beautiful array as defined in the problem description, where 1 <= n <= 3 * 10^5 and 1 <= a_i <= n. The function should also handle multiple test cases, where the number of test cases `t` is an integer such that 1 <= t <= 10^4. The sum of `n` over all test cases does not exceed 3 * 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `n` is the same as the input, `i` is `n-1`, `arr` is the same as the input list of integers provided by the user, and `flag` is `True` if all elements in `arr` are the same, otherwise `flag` is `False`.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: `n` is the same as the input, `i` is `n-1`, `arr` is the same as the input list of integers provided by the user, `flag` is `True` if all elements in `arr` are the same, otherwise `flag` is `False`, `val` is the first element of `arr`. `cnt` is the number of times the first element `val` appears consecutively from the start of the array. `ans` is the minimum count of consecutive `val` appearances before a different element is encountered, or `Decimal('Infinity')` if all elements are the same.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: min(ans, cnt) (where ans is the previous value of ans and cnt is the number of times the first element of arr appears consecutively from the start of the array)
    #State: *`n` is the same as the input, `i` is `n-1`, `arr` is the same as the input list of integers provided by the user, `val` is the first element of `arr`, `cnt` is the number of times the first element `val` appears consecutively from the start of the array, and `ans` is the minimum of the previous `ans` value and `cnt`. If all elements in `arr` are the same, `flag` is `True`. Otherwise, `flag` is `False`.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `arr` from the user. It checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it finds the minimum number of consecutive occurrences of the first element in `arr` before a different element is encountered, and prints this value. The function does not return any value; it only prints the result. The state of the program after the function concludes includes the original `n` and `arr` values, a `flag` indicating whether all elements in `arr` are the same, and `ans` which holds the minimum count of consecutive first elements or `Decimal('Infinity')` if all elements are the same.

