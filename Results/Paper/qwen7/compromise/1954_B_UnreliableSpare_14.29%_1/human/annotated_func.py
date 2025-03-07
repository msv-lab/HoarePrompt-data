#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5; the array a is a list of n integers such that 1 ≤ a_i ≤ n and the array is beautiful; the sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: `flag` is False, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 ⋅ 10^5, `arr` is a list of integers obtained from splitting the input string by spaces and converting each element to an integer.
    #
    #Explanation: The loop checks if the current element in the list `arr` is different from the previous one. If it finds any difference, it sets `flag` to `False` and breaks out of the loop. Therefore, `flag` will be `False` if there is at least one pair of consecutive elements in `arr` that are different. If all elements are the same, `flag` remains `True`.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: Output State: `flag` is False, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 ⋅ 10^5, `arr` is a list of integers obtained from splitting the input string by spaces and converting each element to an integer, `val` is the first element of `arr`, `cnt` is the maximum number of consecutive occurrences of `val` in `arr`, `ans` is the minimum value of `cnt` encountered during the loop execution.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum value between the initial value and the maximum number of consecutive occurrences of val in arr)
    #State: `flag` is either True or False, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 ⋅ 10^5, `arr` is a list of integers obtained from splitting the input string by spaces and converting each element to an integer, `val` is the first element of `arr`, `cnt` is the maximum number of consecutive occurrences of `val` in `arr`, `ans` is updated to be the minimum value between the current `ans` and `cnt`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( t \) (1 ≤ \( t \) ≤ 10^4), an integer \( n \) (1 ≤ \( n \) ≤ 3 ⋅ 10^5), and an array \( a \) of \( n \) integers (1 ≤ \( a_i \) ≤ \( n \)). The function determines whether the array \( a \) is uniform (all elements are the same) or not. If the array is uniform, it prints -1. Otherwise, it calculates the minimum length of the longest sequence of identical elements in the array and prints this value.

