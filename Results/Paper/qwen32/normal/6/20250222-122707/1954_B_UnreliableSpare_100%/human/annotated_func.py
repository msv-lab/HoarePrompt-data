#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 3 \cdot 10^5, and a is a list of n integers where each element a_i satisfies 1 <= a_i <= n. The array a is guaranteed to be beautiful. The sum of n over all test cases does not exceed 3 \cdot 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer, `a` is a list of `n` integers where each element `a_i` satisfies 1 <= `a_i` <= `n`, `arr` is a list of integers read from the input, `flag` is True if all elements in `arr` are the same, otherwise `flag` is False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer, `a` is a list of `n` integers where each element `a_i` satisfies 1 <= `a_i` <= `n`, `arr` is a list of integers read from the input, `flag` is True if all elements in `arr` are the same, otherwise `flag` is False, `val` is `arr[0]`, `cnt` is the length of the last sequence of consecutive elements equal to `val` if the loop ends with a sequence of such elements, `ans` is the length of the shortest sequence of consecutive elements equal to `val` encountered during the loop, or it will remain Decimal('Infinity') if no such sequence was found, `i` is `n-1`.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum length of consecutive sequences of the same element in the list `arr`)
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer, `a` is a list of `n` integers where each element `a_i` satisfies 1 <= `a_i` <= `n`, `arr` is a list of integers read from the input, `flag` is a boolean indicating whether all elements in `arr` are the same, `val` is `arr[0]`, `cnt` is the length of the last sequence of consecutive elements equal to `val` if the loop ends with a sequence of such elements, `ans` is the minimum of its previous value and `cnt`, `i` is `n-1`. If `flag` is True, all elements in `arr` are the same. Otherwise, not all elements in `arr` are the same.
#Overall this is what the function does:The function reads an integer `n` and a list `arr` of `n` integers from the input. It determines if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it calculates and prints the length of the shortest sequence of consecutive elements that are the same in the list.

