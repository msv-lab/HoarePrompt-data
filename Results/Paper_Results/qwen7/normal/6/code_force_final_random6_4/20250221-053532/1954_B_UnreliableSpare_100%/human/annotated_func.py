#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the array a is beautiful.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: After the loop executes all iterations, `i` is equal to `n-1`, `n` must be greater than 1, and `flag` remains False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: After the loop executes all iterations, `i` will be equal to `n`, `flag` remains False, `ans` will hold the minimum value of `cnt` encountered during the loop, `val` will be the initial value of `arr[0]`, and `cnt` will be 0.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: 0
    #State: Postcondition: `ans` is updated to the minimum value between its current value and `cnt`, `flag` remains False, `val` is the initial value of `arr[0]`, and `cnt` remains 0.
#Overall this is what the function does:The function processes an input array `a` of length `n` (1 ≤ n ≤ 3 * 10^5) to determine if it is beautiful. If the array is not constant (i.e., not all elements are the same), it finds and prints the minimum consecutive segment length where the elements are the same. If the array is constant, it prints -1.

