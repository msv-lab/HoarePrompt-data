#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5; the array a is a list of n integers such that 1 ≤ a_i ≤ n and the array a is beautiful; the sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: The loop has executed all iterations. The value of `i` is `n-1`, `n` remains as the original input integer, `arr[i]` is not equal to `arr[i - 1]`, and `flag` remains False since no break occurs in the if condition throughout all iterations.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: After the loop executes all iterations, `arr` is a list of integers, `ans` is updated to the minimum value between its current value and `cnt` for each iteration, `cnt` is incremented by 1 for each element in `arr`, and `i` is equal to `n` (the length of `arr`).
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: 0
    #State: Postcondition: `arr` is a list of integers, `ans` is updated to the minimum value between its current value and `cnt` for each iteration, `cnt` is incremented by 1 for each element in `arr`, and `i` is equal to `n` (the length of `arr`). Whether `flag` is True or False, `ans` reflects the minimum value between its initial value and the count of elements processed in `arr`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( n \) and an array \( a \) of \( n \) integers. It first checks if the array \( a \) is monotonous (i.e., all elements are the same). If the array is not monotonous, it calculates the minimum number of changes required to make the array monotonous. If the array is monotonous, it prints -1; otherwise, it prints the calculated minimum number of changes.

