#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n. Additionally, the sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the sum of `n` over all test cases does not exceed 3 \cdot 10^5; additionally, `arr` is a list of integers obtained by splitting the input and converting each element to an integer; `flag` is set to False if there is at least one pair of consecutive elements in `arr` that are not equal, otherwise `flag` is set to True.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: Output State: `val` is equal to `arr[n-1]`, `cnt` is 0, `flag` is True, `ans` is the minimum count of consecutive equal elements found during the loop execution.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: 0
    #State: `val` is equal to `arr[n-1]`, `cnt` is 0, `flag` is True/False, `ans` is the minimum count of consecutive equal elements found during the loop execution, and `ans` is updated to the minimum between its current value and `cnt`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer n and a list of n integers. It checks if all elements in the list are identical. If they are, it prints -1. Otherwise, it finds the minimum length of consecutive identical elements in the list and prints this value. The function does not return any value but prints the result directly.

