#State of the program right berfore the function call: The function should accept a list of integers `a` and an integer `n` such that 1 ≤ n ≤ 3 · 10^5 and 1 ≤ a_i ≤ n, and the array `a` is guaranteed to be beautiful. The function should also handle multiple test cases, indicated by an integer `t` where 1 ≤ t ≤ 10^4, and the sum of `n` over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: The value of `flag` will be `False` if any two consecutive elements in the list `arr` are different. Otherwise, `flag` will remain `True`. The values of `n` and `arr` will remain unchanged.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: `flag` remains unchanged, `n` remains unchanged, `arr` remains unchanged, `ans` is the minimum count of consecutive elements equal to the first element of `arr` before a different element is encountered, `val` is the first element of `arr`, and `cnt` is the count of consecutive elements equal to the first element of `arr` at the end of the list or before a different element is encountered.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: - The `print(ans)` statement will print the value of `ans`, which is the minimum count of consecutive elements equal to the first element of `arr` before a different element is encountered or the value of `cnt`, whichever is smaller.
        #
        #Output:
    #State: *`flag` remains unchanged, `n` remains unchanged, `arr` remains unchanged, `ans` is the minimum count of consecutive elements equal to the first element of `arr` before a different element is encountered or the value of `cnt`, whichever is smaller, `val` is the first element of `arr`, and `cnt` is the count of consecutive elements equal to the first element of `arr` at the end of the list or before a different element is encountered.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each defined by an integer `n` and a list of integers `arr` where 1 ≤ n ≤ 3 · 10^5 and 1 ≤ a_i ≤ n. The function checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it calculates and prints the minimum count of consecutive elements equal to the first element of `arr` before a different element is encountered. The function does not modify the input variables `n` or `arr`.

