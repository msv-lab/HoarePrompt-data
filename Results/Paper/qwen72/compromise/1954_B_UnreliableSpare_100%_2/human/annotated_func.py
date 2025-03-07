#State of the program right berfore the function call: The function should accept two parameters: a list of integers `a` and an integer `n` representing the length of the list `a`. The list `a` is a beautiful array as defined in the problem, and `1 <= n <= 3 * 10^5`. The function should also handle multiple test cases, where the number of test cases `t` is an integer such that `1 <= t <= 10^4`. The sum of `n` over all test cases does not exceed `3 * 10^5`.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: The list `a` remains a beautiful array, `1 <= n <= 3 * 10^5`, `1 <= t <= 10^4`, `n` is an input integer, `arr` is a list of integers obtained from the input, `flag` is False if any element in `arr` is different from its previous element, otherwise `flag` remains True.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `ans` is the minimum length of consecutive elements that are the same as `val` in `arr`, `cnt` is the count of the last sequence of consecutive elements that are the same as `val` (or 0 if the last element is not `val`), `val` is the first element of `arr`, `flag` remains unchanged, `n` remains unchanged, `arr` remains unchanged.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: - Since the exact values of `arr` and the previous `ans` are not provided, we can only describe the output in terms of the given variables and conditions.
        #   - The print statement will output the value of `ans`, which is the minimum of the previous `ans` and `cnt`.
        #
        #Output:
    #State: *`ans` is the minimum of the previous `ans` and `cnt`, `cnt` is the count of the last sequence of consecutive elements that are the same as `val` (or 0 if the last element is not `val`), `val` is the first element of `arr`, `flag` remains unchanged, `n` remains unchanged, and `arr` remains unchanged.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each containing a list of integers `arr` and an integer `n` representing the length of the list. It checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it finds the minimum length of consecutive elements that are the same as the first element in `arr` and prints this value. The function does not modify the input list `arr` or the integer `n`.

