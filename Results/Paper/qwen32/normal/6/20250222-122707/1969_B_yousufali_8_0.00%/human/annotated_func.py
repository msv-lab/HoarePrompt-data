#State of the program right berfore the function call: s is a list of integers where each integer is either 0 or 1, representing a binary string. n is an integer initialized to 0, and ans is an integer initialized to 0. The function iterates over the list s to calculate a value based on the number of 1s encountered before each 0.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: `s` is the original binary list, `n` is the count of consecutive 1s at the end of the list (or 0 if the last element is 0), and `ans` is the total count of substrings of 1s ending at each 0 encountered in the list.
    print(ans)
    #This is printed: ans (where ans is the total count of substrings of 1s ending at each 0 encountered in the list `s`)
#Overall this is what the function does:The function calculates and returns the total count of substrings of consecutive 1s that end at each 0 in the given binary list `s`.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an input integer and `func_1()` has been called `t` times.
#Overall this is what the function does:The function `func_2` prompts the user to input an integer `t` and then calls the function `func_1` exactly `t` times. It does not accept any parameters and does not return any value.

