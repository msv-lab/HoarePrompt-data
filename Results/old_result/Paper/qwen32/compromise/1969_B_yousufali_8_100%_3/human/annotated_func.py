#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's), and n and ans are non-negative integers initialized to 0.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: s is a binary string provided by the user input, n is 0, ans is the accumulated sum of (n + 1) for each sequence of '1's followed by a '0'.
    print(ans)
    #This is printed: ans (where ans is the accumulated sum of (n + 1) for each sequence of '1's followed by a '0' in the binary string `s`)
#Overall this is what the function does:The function reads a binary string from user input and calculates the accumulated sum of (n + 1) for each sequence of consecutive '1's followed by a '0', where n is the count of '1's in the sequence. It then prints this accumulated sum.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`. The function does not take any parameters and does not return any value. It reads the number of test cases and iterates through each test case, calling `func_1()` for each one.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is unchanged and `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` reads an integer input representing the number of test cases, and for each test case, it calls the function `func_1`. It does not accept any parameters or return any value.

