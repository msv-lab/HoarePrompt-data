#State of the program right berfore the function call: The function `func_1` is expected to take input parameters, but the function definition provided does not include any parameters. The correct function definition should include parameters for the number of test cases `t` and the arrays `a` for each test case, where `t` is an integer such that 1 ≤ t ≤ 10^4, and for each test case, `n` is an integer such that 1 ≤ n ≤ 3·10^5, and `a` is a list of integers of length `n` where 1 ≤ a_i ≤ n, and the array `a` is guaranteed to be beautiful.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: `n` is an input integer, `t` is an integer such that 1 ≤ t ≤ 10^4, `arr` is a list of integers input by the user, `i` is `n-1` if the loop completes without breaking, or the index at which `arr[i]` is not equal to `arr[i-1]` if the loop breaks. `flag` is True if all elements in `arr` from index 1 to `n-1` are equal to their previous element, otherwise `flag` is False.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: `n` is the input integer, `t` is an integer such that 1 ≤ t ≤ 10^4, `arr` is a list of integers input by the user, `i` is `n-1`, `flag` is True if all elements in `arr` from index 1 to `n-1` are equal to their previous element, otherwise `flag` is False, `val` is the first element of `arr`, `cnt` is the number of consecutive elements from the last change (or 0 if the last element is not equal to `val`), and `ans` is the minimum count of consecutive elements equal to `val` found in the array.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum count of consecutive elements equal to the first element of `arr` found in the array)
    #State: *`n` is the input integer, `t` is an integer such that 1 ≤ t ≤ 10^4, `arr` is a list of integers input by the user, `i` is `n-1`, `val` is the first element of `arr`, and `ans` is the minimum count of consecutive elements equal to `val` found in the array, updated to be the minimum of the previous `ans` and `cnt`. If `flag` is True, it indicates that all elements in `arr` from index 1 to `n-1` are equal to their previous element. If `flag` is False, it indicates that not all elements in `arr` from index 1 to `n-1` are equal to their previous element.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `arr` from the user. It then checks if all elements in `arr` are the same. If they are, it prints `-1`. Otherwise, it calculates the minimum length of consecutive subarrays where the elements are equal to the first element of `arr` and prints this minimum length. The function does not return any value. After the function concludes, `n` and `arr` retain their input values, and the program state includes the printed output, which is either `-1` or the minimum length of consecutive subarrays as described.

