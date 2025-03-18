#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n. The given array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: `flag` is `False`, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, and `arr` is a list of n integers obtained from the input split and converted to integers.
    #
    #Explanation: The loop checks if each element in the array `arr` is different from its previous element. If any two consecutive elements are different, it sets `flag` to `False` and breaks out of the loop. Therefore, the final state of `flag` will be `False` if there is at least one pair of consecutive elements that are different. The values of `t`, `n`, and `arr` remain unchanged as they are not affected by the loop.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: Output State: `flag` is `False`, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `arr` is a list of n integers obtained from the input split and converted to integers, `val` is the first element of `arr`, `cnt` is the maximum count of consecutive occurrences of `val` in `arr`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum value between its initial value and the maximum count of consecutive occurrences of val in arr)
    #State: `flag` is either `True` or `False`. Regardless of the value of `flag`, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `arr` is a list of n integers obtained from the input split and converted to integers, `val` is the first element of `arr`, `cnt` is the maximum count of consecutive occurrences of `val` in `arr`, and `ans` is updated to be the minimum of its current value and `cnt`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `n`, an array `arr` of `n` integers, and an integer `t`. It determines whether all elements in the array `arr` are identical. If they are, it calculates the longest sequence of consecutive identical elements in the array. If any two consecutive elements differ, it prints `-1`. Otherwise, it prints the length of the longest sequence of consecutive identical elements.

