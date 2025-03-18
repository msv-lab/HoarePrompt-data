#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is the input integer such that 1 ≤ n ≤ 3 · 10^5; `a` is a list of n integers where 1 ≤ a_i ≤ n; `arr` is a list of n integers where 1 ≤ arr_i ≤ n and `arr` is equivalent to `a`; `flag` is True if all elements in `arr` are the same, otherwise False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is the input integer such that 1 ≤ n ≤ 3 · 10^5; `a` is a list of n integers where 1 ≤ a_i ≤ n; `arr` is a list of n integers where 1 ≤ arr_i ≤ n and `arr` is equivalent to `a`; `flag` is True if all elements in `arr` are the same, otherwise False; `ans` is the minimum length of any sequence of identical elements in `arr`; `val` is `arr[0]`; `cnt` is the length of the last sequence of identical elements; `i` is `n-1`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum length of any sequence of identical elements in the list `arr`)
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is the input integer such that 1 ≤ n ≤ 3 · 10^5; `a` is a list of n integers where 1 ≤ a_i ≤ n; `arr` is a list of n integers where 1 ≤ arr_i ≤ n and `arr` is equivalent to `a`; `flag` is True if all elements in `arr` are the same, otherwise False; `ans` is the minimum value between the previous `ans` and `cnt`; `val` is `arr[0]`; `cnt` is the length of the last sequence of identical elements, which is equal to `n` if all elements in `arr` are the same, otherwise it is the length of the last sequence of identical elements before the condition was met; `i` is `n-1`.
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers. It determines if all elements in the list are the same. If they are, it prints `-1`. Otherwise, it finds and prints the minimum length of any sequence of identical consecutive elements in the list.

