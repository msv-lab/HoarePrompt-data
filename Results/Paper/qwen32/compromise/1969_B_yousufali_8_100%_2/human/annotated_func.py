#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's), and n is initialized to 0 and ans is initialized to 0.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: s is the user input, n is 1, ans is 5.
    print(ans)
    #This is printed: 5
#Overall this is what the function does:The function `func_1` reads a binary string from user input, processes it, and prints the computed value of `ans`, which represents the sum of counts of consecutive '1's incremented by one each time a '0' is encountered after a sequence of '1's.

#State of the program right berfore the function call: No variables in the function signature.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an input integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It prompts the user to input an integer `t` and then calls `func_1` exactly `t` times. The function itself does not return any value but may perform actions within `func_1` for each iteration.

