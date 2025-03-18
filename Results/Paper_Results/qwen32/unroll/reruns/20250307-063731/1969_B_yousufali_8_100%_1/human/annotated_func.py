#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's), and n is initialized to 0 and ans is initialized to 0. The function iterates over each character in s, updating n and ans based on the conditions specified within the loop.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: s is the input binary string, n is the total count of '1's in s, ans is the accumulated sum of (n + 1) for each '0' encountered after one or more '1's.
    print(ans)
    #This is printed: ans (where ans is the accumulated sum of (n + 1) for each '0' encountered after one or more '1's in the binary string `s`)
#Overall this is what the function does:The function reads a binary string from the input, counts the number of '1's encountered, and calculates the accumulated sum of (count of '1's + 1) each time a '0' is encountered after one or more '1's. It then prints this accumulated sum.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an input integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from the user, then calls `func_1` a total of `t` times. The function does not return any value but performs actions based on the logic defined within `func_1`.

