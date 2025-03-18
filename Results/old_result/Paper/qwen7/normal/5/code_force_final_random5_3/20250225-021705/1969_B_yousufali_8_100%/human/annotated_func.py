#State of the program right berfore the function call: s is a binary string (consisting only of '0's and '1's), and n is an integer representing the count of '1's encountered up to the current index during iteration.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: After the loop executes all iterations, `i` will be equal to the length of `s`, `n` will be the count of '1's in the string `s`, and `ans` will be the sum of `n + 1` for each occurrence of '0' followed by a '1'.
    print(ans)
    #This is printed: ans (where ans is the sum of n + 1 for each occurrence of '0' followed by a '1' in the string s)
#Overall this is what the function does:The function accepts a binary string `s` and calculates the sum of `n + 1` for each occurrence of '0' followed by a '1' in the string. It then prints this sum.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, the input is a binary string s (2 ≤ |s| ≤ 2⋅10^5) consisting of only '0's and '1's.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` must be greater than 0.
    #
    #In natural language: The value of `t` must remain greater than 0 after all the iterations of the loop have finished. This is because the loop continues to execute as long as `t` is greater than 0, and there are no operations within the loop that change the value of `t`.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it processes a binary string `s` (2 ≤ |s| ≤ 2⋅10^5) consisting of only '0's and '1's by calling `func_1()`. After processing all test cases, the value of `t` remains greater than 0.

