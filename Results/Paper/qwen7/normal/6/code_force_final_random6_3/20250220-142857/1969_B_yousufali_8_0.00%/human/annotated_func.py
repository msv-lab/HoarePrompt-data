#State of the program right berfore the function call: s is a binary string (consisting only of '0's and '1's) and its length is at least 2.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: Output State: The value of `ans` is the sum of `n + 1` for every occurrence of '0' following one or more '1's in the list `s`, plus any individual '1's encountered. The variable `i` will be equal to the length of the list `s`, and `n` will be the count of '1's in the list `s`.
    #
    #In simpler terms, `ans` will be the total count of segments where there are one or more '1's followed by a '0', plus one additional count for each standalone '1'. The variable `i` will reflect the total number of elements processed in the list `s`, and `n` will give the total number of '1's found in the list `s`.
    print(ans)
    #This is printed: 8
#Overall this is what the function does:The function processes a binary string `s` to count the number of segments where there are one or more '1's followed by a '0', plus one additional count for each standalone '1'. It prints the total count of such segments. The function does not accept any parameters and does not return any value.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, a binary string s is provided where 2 ≤ |s| ≤ 2 ⋅ 10^5 and s consists only of '0' and '1'.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` must be greater than 0.
    #
    #In natural language: The value of `t` must remain greater than 0 after all the iterations of the loop have finished. This is because the loop continues to execute as long as `t` is greater than 0, and there are no operations within the loop that modify the value of `t`.
#Overall this is what the function does:The function processes a specified number of test cases (`t`). For each test case, it calls another function `func_1()` to process a binary string `s`. After processing all test cases, the function ensures that the variable `t` remains greater than 0.

