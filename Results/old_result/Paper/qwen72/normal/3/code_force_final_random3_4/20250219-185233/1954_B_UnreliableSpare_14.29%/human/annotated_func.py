#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list represents a test case and contains integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) for a beautiful array of length n (1 ≤ n ≤ 3 · 10^5). The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `t` is an integer between 1 and 10^4, `arr` is a list of integers, the sum of the lengths of all inner lists in the input list does not exceed 3 · 10^5, `i` is `n-1`, `n` is the length of `arr`, and `flag` is True if all elements in `arr` are the same; otherwise, `flag` is False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: `t` is an integer between 1 and 10^4, `arr` is a list of integers, the sum of the lengths of all inner lists in the input list does not exceed 3 · 10^5, `i` is `n-1`, `n` is the length of `arr` and must be greater than 0, `flag` is True if all elements in `arr` are the same; otherwise, `flag` is False, `val` is the first element of `arr`. `cnt` is the number of consecutive elements from the start of `arr` that are equal to `val` before encountering a different element, or `n` if all elements are equal to `val`. `ans` is the minimum value between Decimal('Infinity') and the length of the longest prefix of `arr` where all elements are equal to `val` before encountering a different element. If all elements in `arr` are equal to `val`, `ans` remains Decimal('Infinity').
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: Output:
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum value between the previous ans and cnt, and cnt is the number of consecutive elements from the start of arr that are equal to val)
    #State: *`t` is an integer between 1 and 10^4, `arr` is a list of integers, the sum of the lengths of all inner lists in the input list does not exceed 3 · 10^5, `i` is `n-1`, `n` is the length of `arr` and must be greater than 0, `val` is the first element of `arr`, `cnt` is the number of consecutive elements from the start of `arr` that are equal to `val` before encountering a different element, or `n` if all elements are equal to `val`, and `ans` is the minimum value between the previous `ans` and `cnt`. If `flag` is True, `cnt` is `n` because all elements in `arr` are equal to `val`.
#Overall this is what the function does:The function reads an integer `n` and a list of integers `arr` from the user. It checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it calculates the minimum length of consecutive elements from the start of `arr` that are equal to the first element, and prints this minimum length. The function does not return any value, but it prints the result to the console.

