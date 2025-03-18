#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The given array a is beautiful according to the problem's definition, and the sum of n over all test cases does not exceed 3 * 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is the input integer; `a` is a list of `n` integers where 1 <= a_i <= n; `arr` is a list of integers derived from the input; `flag` is True if all elements in `arr` are the same, otherwise `flag` is False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is the input integer; `a` is a list of `n` integers where 1 <= a_i <= n; `arr` is a list of integers derived from the input; `flag` is True if all elements in `arr` are the same, otherwise `flag` is False; `ans` is the length of the shortest sequence of consecutive elements in `arr` that are equal to `val` before a different element is encountered, or `Decimal('Infinity')` if all elements in `arr` are the same; `val` is the last encountered value in `arr` that started a sequence counted by `cnt`; `cnt` is the count of the final sequence of elements in `arr` that are equal to the last encountered `val`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum of its previous value and cnt)
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is the input integer; `a` is a list of `n` integers where 1 <= a_i <= n; `arr` is a list of integers derived from the input; `flag` is a boolean indicating whether all elements in `arr` are the same; `ans` is the minimum of its previous value and `cnt`; `val` is the last encountered value in `arr` that started a sequence counted by `cnt`; `cnt` is the count of the final sequence of elements in `arr` that are equal to the last encountered `val`.
#Overall this is what the function does:The function reads an integer `n` and a list `arr` of `n` integers. It determines if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it finds and prints the length of the shortest sequence of consecutive elements in `arr` that are the same before a different element is encountered.

