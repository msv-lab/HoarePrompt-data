#State of the program right berfore the function call: s is a binary string (a string consisting of only '0's and '1's), and n is an integer representing the number of times a '1' is encountered before a '0'. ans is an integer representing the total cost to sort the string using cyclic shifts.
def func_1():
    s = input()
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '1':
            n += 1
        
        if s[i] == '0' and n != 0:
            ans += n + 1
        
    #State: Output State: `s` is a binary string, `n` is 0, and `ans` is the sum of all substrings starting from a '1' and ending just before a '0'.
    print(ans)
    #This is printed: ans (where ans is the sum of all substrings starting from a '1' and ending just before a '0' in the binary string s)
#Overall this is what the function does:The function accepts a binary string `s` and calculates the total cost to sort the string using cyclic shifts. Specifically, it computes the sum of all substrings starting from a '1' and ending just before a '0'. The function then prints this total cost.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, a binary string s is provided on a new line with 2 <= |s| <= 2 * 10^5, where each character in s is either '0' or '1'.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t remains the same integer it was initialized as, and no other variables are mentioned as being affected by the loop. The function `func_1()` is called t times, but its effects are not specified.
#Overall this is what the function does:The function processes a specified number of test cases (t). For each test case, it reads a binary string (s) and calls another function `func_1()`. After processing all test cases, the function does not return any value.

