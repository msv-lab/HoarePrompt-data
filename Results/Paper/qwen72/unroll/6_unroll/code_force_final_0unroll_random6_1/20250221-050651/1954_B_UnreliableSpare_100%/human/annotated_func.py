#State of the program right berfore the function call: The function should take two parameters: a list of integers `a` and an integer `n` representing the length of the list `a`. The list `a` is a beautiful array with elements in the range 1 to n, and the integer `n` satisfies 1 ≤ n ≤ 3·10^5. Additionally, the function should handle multiple test cases, indicated by an integer `t` where 1 ≤ t ≤ 10^4, and the sum of `n` over all test cases does not exceed 3·10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: Output State: The value of `flag` will be **False** if there is at least one pair of consecutive elements in the list `arr` that are not equal. Otherwise, if all consecutive elements in the list `arr` are equal, `flag` will remain **True**. The values of `i`, `n`, and `arr` will remain unchanged.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
            cnt = 0
        
    #State: The value of `flag` remains unchanged from the initial state. The value of `ans` is the minimum count of consecutive elements that are equal to `val` (which is `arr[0]`) found in the list `arr`. The value of `cnt` is the count of consecutive elements equal to `val` at the end of the list `arr`. The values of `i`, `n`, and `arr` remain unchanged.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum of the initial value of ans and the count of consecutive elements equal to val at the end of the list arr)
    #State: *The value of `flag` remains unchanged from the initial state. The value of `ans` is the minimum of the initial `ans` and `cnt`. The value of `cnt` is the count of consecutive elements equal to `val` at the end of the list `arr`. The values of `i`, `n`, and `arr` remain unchanged.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `arr` from the input. It checks if all elements in `arr` are equal. If they are, it prints `-1`. If not, it calculates the minimum count of consecutive elements that are equal to the first element of `arr` and prints this count. The function does not return any value; it only prints the result. The function is designed to handle multiple test cases, but the code provided does not explicitly manage the test cases or validate input constraints.

