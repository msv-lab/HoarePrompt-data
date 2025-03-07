#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` representing the beautiful array, and an integer `n` representing the length of the array. The array `a` is guaranteed to be beautiful, and `n` satisfies 1 ≤ n ≤ 3 · 10^5. The function should also handle multiple test cases, indicated by an integer `t` (1 ≤ t ≤ 10^4) provided as an input parameter. The sum of `n` over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: The value of `flag` will be `False` if any two consecutive elements in `arr` are different. Otherwise, `flag` will remain `True`. The values of `i`, `n`, and `arr` will remain unchanged.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: `flag` remains `False` if any two consecutive elements in `arr` are different; otherwise, `flag` remains `True`. The values of `i`, `n`, and `arr` remain unchanged. `ans` is the minimum count of consecutive elements equal to `arr[0]` before a different element is encountered. `val` is `arr[0]`, and `cnt` is the count of consecutive elements equal to `arr[0]` at the end of the loop.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the count of consecutive elements equal to arr[0] at the beginning of the list arr)
    #State: *`flag` remains `False` if any two consecutive elements in `arr` are different; otherwise, `flag` remains `True`. The values of `i`, `n`, and `arr` remain unchanged. `ans` is the minimum count of consecutive elements equal to `arr[0]` before a different element is encountered. `val` is `arr[0]`, and `cnt` is the count of consecutive elements equal to `arr[0]` at the end of the loop. If `flag` is `True`, `ans` is updated to the minimum value between the original `ans` and `cnt`. If `flag` is `False`, `ans` remains the minimum count of consecutive elements equal to `arr[0]` before a different element is encountered.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a list of integers `arr`. It checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it calculates the minimum count of consecutive elements equal to the first element of `arr` before a different element is encountered and prints this count. The function does not return any value.

