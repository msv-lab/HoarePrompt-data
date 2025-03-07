#State of the program right berfore the function call: The function `func_1` should take two parameters: `t` (an integer where 1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists `arrays` where each inner list represents a beautiful array `a` of integers. Each `a` has a length `n` (1 ≤ n ≤ 3 · 10^5) and contains integers `a_i` (1 ≤ a_i ≤ n). The sum of `n` over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `i` is `n-1`, `n` is an integer where 1 ≤ n ≤ 3 · 10^5, `t` is an integer where 1 ≤ t ≤ 10^4, `arrays` is a list of lists where each inner list represents a beautiful array `a` of integers, `arr` is a list of integers obtained from the input, and `flag` is True if all elements in `arr` are the same, otherwise `flag` is False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `i` is `n-1`, `n` is an integer where 1 ≤ n ≤ 3 · 10^5, `t` is an integer where 1 ≤ t ≤ 10^4, `arrays` is a list of lists where each inner list represents a beautiful array `a` of integers, `arr` is a list of integers obtained from the input, `flag` is True if all elements in `arr` are the same, otherwise `flag` is False, `ans` is the minimum of the counts of consecutive elements equal to `val` before encountering a different element, `val` is the first element of `arr`, `cnt` is the count of consecutive elements equal to `val` at the end of the loop.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum count of consecutive elements equal to the first element of arr before encountering a different element, updated to be the minimum of the previous ans and cnt)
    #State: *`i` is `n-1`, `n` is an integer where 1 ≤ n ≤ 3 · 10^5, `t` is an integer where 1 ≤ t ≤ 10^4, `arrays` is a list of lists where each inner list represents a beautiful array `a` of integers, `arr` is a list of integers obtained from the input, `val` is the first element of `arr`, `cnt` is the count of consecutive elements equal to `val` at the end of the loop, and `ans` is the minimum of the previous `ans` and `cnt`. If `flag` is True (all elements in `arr` are the same), `ans` remains the same as the count of consecutive elements equal to `val`. If `flag` is False (not all elements in `arr` are the same), `ans` is the minimum of the counts of consecutive elements equal to `val` before encountering a different element.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `arr` from the input. It checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it calculates the minimum count of consecutive elements equal to the first element of `arr` before encountering a different element and prints this minimum count. The function does not return any value; it only prints the result.

