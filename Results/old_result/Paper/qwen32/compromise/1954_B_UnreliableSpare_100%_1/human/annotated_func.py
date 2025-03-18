#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The array a is guaranteed to be beautiful. The sum of n over all test cases does not exceed 3 * 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `flag` is `False`.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `flag` is `False`; `ans` is the minimum count of consecutive `val` elements found in the array or `Decimal('Infinity')` if all elements are `val`; `val` is `arr[0]`; `cnt` is the count of consecutive `val` elements at the end of the array.
    #
    #Given the format required:
    #Output State:
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum of its original value and cnt)
    #State: `flag` is `False`; `ans` is the minimum of the original `ans` and `cnt`; `val` is `arr[0]`; `cnt` is the count of consecutive `val` elements at the end of the array. The `flag` remains `False` regardless of the initial value.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it determines if all elements in the list are the same. If they are, it prints `-1`. Otherwise, it finds and prints the minimum length of consecutive elements that are the same in the list.

