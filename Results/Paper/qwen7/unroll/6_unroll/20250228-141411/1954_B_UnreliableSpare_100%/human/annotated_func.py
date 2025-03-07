#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. Additionally, the given array a is beautiful, and the sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 3⋅10^5, `a` is a list of n integers where 1 ≤ a_i ≤ n, `arr` is a list of integers obtained from input split and mapped to integers, `flag` is False.
    #
    #Explanation: The loop checks if the current element in `arr` is different from the previous one. If it finds any two consecutive elements that are different, it sets `flag` to `False` and breaks out of the loop. Therefore, after the loop completes, `flag` will be `False` if there is at least one pair of consecutive elements in `arr` that are different, otherwise, it remains `True`. However, since the problem statement specifies that `flag` is initially `True`, and the loop will set it to `False` as soon as it finds a difference, the final state of `flag` will be `False`.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: Output State: `val` is the last element in `arr`, `cnt` is the count of consecutive occurrences of `val` in `arr`, `ans` is the minimum count of consecutive occurrences of any element in `arr`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum count of consecutive occurrences of val in arr)
    #State: Postcondition: `val` is the last element in `arr`, `cnt` is the count of consecutive occurrences of `val` in `arr`, and `ans` is the minimum of `ans` and `cnt`. Whether `flag` is true or false, `ans` remains the minimum of `ans` and `cnt`.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer n and a list a of n integers. It determines if the list a is "beautiful" (i.e., all elements in the list are the same). If the list is not beautiful, it calculates the minimum number of consecutive occurrences of any element in the list and prints this value. If the list is beautiful, it prints -1.

