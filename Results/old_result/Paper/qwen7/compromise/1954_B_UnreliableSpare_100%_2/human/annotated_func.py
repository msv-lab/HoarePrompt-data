#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The given array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 3 * 10^5, `a` is a list of n integers where 1 ≤ a_i ≤ n, `arr` is a list of integers obtained from the input split and mapped to integers, `flag` is False.
    #
    #Explanation: The loop checks if each element in `arr` is different from its previous element. If any two consecutive elements are different, it sets `flag` to `False` and breaks out of the loop. Therefore, `flag` will be `False` if there is at least one pair of consecutive elements that are different. If all elements are the same or no two consecutive elements are different, `flag` remains `True`.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: Output State: `val` is equal to `arr[0]`, `cnt` is 0, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 3 * 10^5, `a` is a list of n integers where 1 ≤ a_i ≤ n, `arr` is a list of integers obtained from the input split and mapped to integers, `flag` is False, `ans` is the minimum count of consecutive occurrences of `val` in `arr`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the length of the longest sequence of consecutive occurrences of val in arr)
    #State: Postcondition: `val` is equal to `arr[0]`, `cnt` is 0, and `ans` is the minimum count of consecutive occurrences of `val` in `arr`. If the flag is True, `ans` is updated by 1 if `cnt` was previously assigned a value. Otherwise, `ans` remains unchanged.
#Overall this is what the function does:The function processes a list of integers `a` for each test case defined by an integer `t`. It first checks if the list `a` contains consecutive different elements. If it does, it calculates the minimum count of consecutive occurrences of the initial element in the list. If the list does not contain consecutive different elements, it prints `-1`; otherwise, it prints the length of the longest sequence of consecutive occurrences of the initial element in the list.

