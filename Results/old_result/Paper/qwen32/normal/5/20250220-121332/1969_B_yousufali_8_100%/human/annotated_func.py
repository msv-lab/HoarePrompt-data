#State of the program right berfore the function call: s is a binary string consisting of '0's and '1's, and ans is initialized to 0. n is a counter initialized to 0 and is used to count the number of '1's encountered before a '0'.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `ans` is the final accumulated sum, and `n` is the count of trailing '1's if the string ends with '1'.
    print(ans)
    #This is printed: ans (where ans is the final accumulated sum)
#Overall this is what the function does:The function `func_1` reads a binary string `s` from the input, processes it to count consecutive '1's before each '0', and prints the accumulated sum of these counts plus one for each '0' encountered. If the string ends with '1's, it adds the count of these trailing '1's to the sum. The function does not accept any parameters and does not return a value; it directly prints the result.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`, hence no precondition can be derived from it.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an input integer that must be greater than or equal to 0; `func_1()` has been executed `t` times.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, which represents the number of times to execute `func_1`. It does not accept any parameters and does not return any value explicitly. The function's final state involves having executed `func_1` exactly `t` times.

