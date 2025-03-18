#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The array a is guaranteed to be beautiful according to the problem's definition. The sum of n over all test cases does not exceed 3 * 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Since the loop only modifies the `flag` variable, and the values of `t`, `n`, `a`, and `arr` are not affected by the loop, the output state will be:
    #
    #- `t` remains the same.
    #- `n` remains the same.
    #- `a` remains the same.
    #- `arr` remains the same.
    #- `flag` will be `True` if all elements in `arr` are the same; otherwise, `flag` will be `False`.
    #
    #Output State:
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: - `ans` will be the minimum count of consecutive elements equal to `val` before a different element is encountered, or `Decimal('Infinity')` if all elements are equal to `val`.
    #- `val` remains `arr[0]`.
    #- `cnt` will be the count of the last sequence of consecutive elements equal to `val`.
    #
    #However, without the specific array `arr` and the value of `n`, we cannot determine a specific numerical value for `ans` and `cnt`. Therefore, the most accurate output state we can specify based on the given information is:
    #
    #Output State:
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum of its previous value and cnt)
    #State: `ans` is the minimum of the previous `ans` and `cnt`; `val` remains `arr[0]`; `cnt` remains unchanged; `flag` is either `True` or `False` depending on the condition evaluated.
#Overall this is what the function does:The function reads an integer `n` and a list `arr` of `n` integers. It checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it finds and prints the minimum length of any contiguous subarray within `arr` where all elements are the same.

