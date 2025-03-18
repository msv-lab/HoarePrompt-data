#State of the program right berfore the function call: s is a binary string (consisting only of '0's and '1's), and n is an integer representing the count of '1's encountered until the current index, initialized to 0. ans is an integer representing the total cost, also initialized to 0.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: Output State: `s` is an input string, `n` is equal to the length of `s`, `ans` is the sum of `n + 1` for each occurrence of '0' in `s` followed by a '1', and `i` is the last index of the string `s`.
    #
    #In simpler terms, after the loop has executed all its iterations, the variable `n` will hold the total length of the string `s`. The variable `ans` will contain the count of segments in the string where a '0' is immediately followed by one or more '1's, plus one for each such segment. The variable `i` will be set to the index of the last character in the string `s`.
    print(ans)
    #This is printed: ans (where ans is the sum of n + 1 for each occurrence of '0' immediately followed by one or more '1's in s)
#Overall this is what the function does:The function processes a binary string `s`, counting the number of '1's encountered. It then calculates and returns the total cost `ans`, which is the sum of `n + 1` for each occurrence of '0' immediately followed by one or more '1's in the string. After processing the entire string, the function prints the total cost `ans`.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, a binary string s is provided on a new line where 2 ≤ |s| ≤ 2 ⋅ 10^5 and s consists only of '0' and '1'.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` must be greater than 0.
    #
    #In natural language: The value of `t` must be greater than 0 after the loop has executed all its iterations. This is because the loop continues to run as long as `t` is greater than 0, and since the loop has completed all its iterations, it means `t` was initially greater than 0 and has not been reduced to 0 or below within the loop.
#Overall this is what the function does:The function accepts an integer `t`, representing the number of test cases. For each test case, it calls `func_1()` with a binary string `s` as input, where the length of `s` is between 2 and 200,000 characters, and `s` consists only of '0' and '1'. After processing all test cases, the function does not return any value.

