#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n. The given array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: `flag` is False, t remains unchanged, n remains unchanged, arr remains unchanged.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: Output State: `flag` is False, `t` remains unchanged, `n` remains unchanged, `arr` remains unchanged, `val` is equal to `arr[0]`, `cnt` is 0, `ans` is equal to 0.
    #
    #Explanation: The loop iterates through the array `arr`. Since the initial value of `val` is set to `arr[0]`, the loop compares each element of `arr` with `arr[0]`. If an element matches `arr[0]`, `cnt` is incremented; otherwise, `ans` is updated to the minimum value between `ans` and `cnt`. However, since `cnt` starts at 0 and is only incremented when elements match `arr[0]`, and there is no decrement or reset of `cnt` within the loop, `cnt` will always be 0 unless there are multiple consecutive matching elements, which would then update `ans` to 1 (since `cnt` would reach 1 before being reset). Given the initial conditions and the lack of any resetting mechanism for `cnt`, `cnt` remains 0 throughout the loop, and `ans` is set to 0 if there are no matching elements.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: 0
    #State: `flag` remains False, `t` remains unchanged, `n` remains unchanged, `arr` remains unchanged, `val` is equal to `arr[0]`, `cnt` is 0, `ans` is equal to 0.
#Overall this is what the function does:The function processes an array `arr` to find the minimum length of consecutive segments where all elements are the same as the first element of the array. If the array is not constant (i.e., contains at least one element different from the first), it prints the minimum segment length; otherwise, it prints -1. The function does not return any value but prints the result directly.

