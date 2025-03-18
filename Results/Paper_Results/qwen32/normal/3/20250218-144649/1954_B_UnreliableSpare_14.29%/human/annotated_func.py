#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n across all test cases does not exceed 3 * 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: flag is True.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: `flag` is True; `ans` is the minimum length of any sequence of consecutive elements not equal to `val` found during the loop, or `Decimal('Infinity')` if no such sequence is found; `val` is `arr[0]`; `cnt` is the length of the longest sequence of consecutive elements starting from `arr[0]` that are equal to `val`; `i` is `n-1`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum of its previous value and the length of the sequence of consecutive elements starting from arr[0] that are equal to arr[0])
    #State: `flag` is either True or False; `ans` is the minimum of the previous `ans` and `cnt`; `val` is `arr[0]`; `cnt` is the length of the longest sequence of consecutive elements starting from `arr[0]` that are equal to `val`; `i` is `n-1`.
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers. It checks if all elements in the list are the same. If they are, it prints `-1`. Otherwise, it finds and prints the minimum length of any sequence of consecutive elements in the list that are not equal to the first element.

