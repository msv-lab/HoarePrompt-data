#State of the program right berfore the function call: s is a binary string consisting of only '0's and '1's, and n is a non-negative integer that counts the number of '1's encountered in the string s up to the current index i.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: `s` is unchanged, `n` is the count of trailing '1's if the last character is '1', otherwise `n` is 0, `ans` is the sum of (number of consecutive '1's + 1) for each sequence of '1's followed by a '0'.
    print(ans)
    #This is printed: ans (where ans is the sum of (number of consecutive '1's + 1) for each sequence of '1's followed by a '0' in the string `s`)
#Overall this is what the function does:The function accepts a binary string `s` and calculates the sum of (number of consecutive '1's + 1) for each sequence of '1's followed by a '0' in the string `s`. It prints this calculated sum.

#State of the program right berfore the function call: No variables in the function signature. The function `func_2` does not take any parameters and operates based on input read from standard input.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an input integer.
#Overall this is what the function does:The function `func_2` reads an integer `t` from standard input, then calls `func_1` a total of `t` times. It does not accept any parameters and does not return any value explicitly.

