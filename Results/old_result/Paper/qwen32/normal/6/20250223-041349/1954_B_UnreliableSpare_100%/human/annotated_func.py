#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers such that 1 <= a_i <= n. The sum of n over all test cases does not exceed 3 * 10^5. The given array a is beautiful.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: t is an integer such that 1 <= t <= 10^4; n is an input integer; a is a list of n integers such that 1 <= a_i <= n; The sum of n over all test cases does not exceed 3 * 10^5; The given array a is beautiful; arr is a list of integers obtained from the input; flag is True if all elements in arr are the same, otherwise False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: t
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum of its previous value and cnt)
    #State: `t` is unchanged; `ans` is the minimum of its previous value and `cnt`. If `flag` is True, it remains True. Otherwise, `flag` is set to False.
#Overall this is what the function does:The function reads an integer `n` and a list `arr` of `n` integers from the input. It then determines if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it finds and prints the minimum length of contiguous subsequences in `arr` where all elements are the same.

