#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; a is a list of n non-negative integers such that 0 ≤ a_i < n, and for each test case, the sum of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: The output state after the loop executes all iterations is as follows: `ans` is a string composed of characters based on the values in the list `s` after processing all elements in `array`. Each character in `ans` corresponds to the cumulative count of indices in `array` plus 97. The list `s` is updated such that each index `j` in `array` has its corresponding value in `s` incremented by the total number of occurrences of `j` in `array`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `l`, a list of `l` non-negative integers, and then constructs a string `ans` based on the cumulative counts of the indices in the list. Specifically, for each integer `j` in the list, it appends the character corresponding to `s[j] + 97` to `ans` and increments `s[j]` by one. After processing all test cases, it prints the constructed string `ans` for each case.

