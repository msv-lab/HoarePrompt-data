#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers such that 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n over all test cases does not exceed 3 * 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is the input integer; `a` is a list of n integers such that 1 <= a_i <= n; `arr` is a list of integers obtained from the input; `flag` is True if all elements in `arr` are the same, otherwise `flag` is False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: t is an integer such that 1 <= t <= 10^4; n is the input integer; a is a list of n integers such that 1 <= a_i <= n; arr is a list of integers obtained from the input; flag is True if all elements in arr are the same, otherwise flag is False; ans is the minimum length of consecutive occurrences of arr[0] before the last sequence (or Decimal('Infinity') if no such sequence exists); val is arr[0]; cnt is the count of the last consecutive sequence of val at the end of arr (if any).
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum of its previous value and the count of the last consecutive sequence of the first element of arr at the end of arr)
#Overall this is what the function does:The function reads an integer `n` and a list `arr` of `n` integers. It checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it calculates and prints the minimum length of consecutive occurrences of the first element of `arr` before the last sequence of that element.

