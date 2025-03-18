#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n across all test cases does not exceed 3 * 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer; `a` is a list of `n` integers where each element `a_i` satisfies 1 <= `a_i` <= `n`; `arr` is a list of integers read from the input; `flag` is True if `arr[0] == arr[1] == ... == arr[n-1]`, otherwise `flag` is False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is greater than 0; `a` is a list of `n` integers where each element `a_i` satisfies 1 <= `a_i` <= `n`; `arr` is a list of integers read from the input; `flag` is True if `arr[0] == arr[1] == ... == arr[n-1]`, otherwise `flag` is False; `val` is `arr[0]`; `i` is `n`; `cnt` is the length of the last sequence of elements equal to `val` if the last sequence is equal to `val`, otherwise `cnt` is 0; `ans` is the minimum length of any sequence of consecutive elements equal to `val` found in `arr`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum length of any sequence of consecutive elements equal to arr[0] found in arr)
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is greater than 0; `a` is a list of `n` integers where each element `a_i` satisfies 1 <= `a_i` <= `n`; `arr` is a list of integers read from the input; `flag` is True if all elements in `arr` are equal, otherwise `flag` is False; `val` is `arr[0]`; `i` is `n`; `cnt` is the length of the last sequence of elements equal to `val`, which is `n` if all elements in `arr` are equal, otherwise it is the length of the last sequence of elements equal to `val`; `ans` is the minimum length of any sequence of consecutive elements equal to `val` found in `arr`, which is `n` if all elements in `arr` are equal, otherwise it is the minimum of its previous value and `cnt`.
#Overall this is what the function does:The function reads an integer `n` and a list `arr` of `n` integers. It determines if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it finds and prints the minimum length of any sequence of consecutive elements that are the same in `arr`.

