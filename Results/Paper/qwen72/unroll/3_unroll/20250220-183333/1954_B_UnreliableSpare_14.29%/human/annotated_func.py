#State of the program right berfore the function call: The function `func_1` is expected to take input parameters, but the function definition provided does not include any parameters. Based on the problem description, the function should take a list of integers `a` and the length of the list `n` as parameters. Additionally, the function is part of a solution that processes multiple test cases, so it should also take the number of test cases `t` as an input, though this is typically handled in the outer loop of the program rather than being passed to the function for each test case. The array `a` is a beautiful array, meaning it can be modified to have all elements the same by performing the specified operation. The length of the array `n` is a positive integer such that 1 ≤ n ≤ 3 · 10^5, and each element `a_i` of the array is a positive integer such that 1 ≤ a_i ≤ n. The sum of `n` over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            flag = False
            break
        
    #State: The value of `n` remains unchanged. The value of `arr` remains unchanged. The value of `flag` will be False if any two consecutive elements in `arr` are different; otherwise, `flag` will remain True.
    ans = Decimal('Infinity')
    val, cnt = arr[0], 0
    for i in range(n):
        if arr[i] == val:
            cnt += 1
        else:
            ans = min(ans, cnt)
        
    #State: The value of `n` remains unchanged. The value of `arr` remains unchanged. The value of `flag` will be False if any two consecutive elements in `arr` are different; otherwise, `flag` will remain True. `ans` is set to the minimum count of consecutive elements that are equal to `val` (the first element of `arr`) found in the array, or remains Decimal('Infinity') if no such consecutive elements are found. `val` is set to the first element of `arr`. `cnt` is set to the count of the last sequence of consecutive elements that are equal to `val` found in the array.
    ans = min(ans, cnt)
    if flag :
        print(-1)
        #This is printed: -1
    else :
        print(ans)
        #This is printed: ans (where ans is the minimum of the previous value of ans and the count of the last sequence of consecutive elements that are equal to the first element of arr)
    #State: *The value of `n` remains unchanged. The value of `arr` remains unchanged. `val` is set to the first element of `arr`. `cnt` is set to the count of the last sequence of consecutive elements that are equal to `val` found in the array. `ans` is set to the minimum of the previous value of `ans` and `cnt`. If `flag` was initially True, it remains True, and all consecutive elements in `arr` are the same. If `flag` was initially False, it remains False, and there are at least two consecutive elements in `arr` that are different.
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `arr` from the user. It checks if all elements in `arr` are the same. If they are, it prints `-1`. If they are not, it calculates the minimum count of consecutive elements that are equal to the first element of `arr` and prints this count. The function does not modify the input `n` or `arr`.

