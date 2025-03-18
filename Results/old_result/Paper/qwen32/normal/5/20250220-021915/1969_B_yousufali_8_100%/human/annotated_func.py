#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's), and n is an integer initialized to 0, which counts the number of '1's encountered in the string s. ans is an integer initialized to 0, which accumulates the total cost to make the string sorted.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: ans is 5, n is 1.
    print(ans)
    #This is printed: 5
#Overall this is what the function does:The function reads a binary string from the input, calculates the cost required to make the string sorted by counting the number of '1's encountered and adding to the cost whenever a '0' is encountered after a '1', and then prints the total cost.

#State of the program right berfore the function call: No variables in the function signature. The function `func_2` does not take any parameters and operates based on input read from standard input.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `func_1()` is called `t` times.
#Overall this is what the function does:The function `func_2` reads an integer `t` from standard input, then calls `func_1` exactly `t` times. The overall effect is determined by the actions performed within `func_1`, which is not detailed here.

