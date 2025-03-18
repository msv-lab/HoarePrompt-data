#State of the program right berfore the function call: s is a list of integers, where each integer is either 0 or 1.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: Output State: `s` is a list of integers, `n` is 0, `ans` is the sum of all segments of consecutive 1's in `s` plus the length of each segment.
    print(ans)
    #This is printed: ans (where ans is the sum of all segments of consecutive 1's in s plus the length of each segment)
#Overall this is what the function does:The function accepts a list of integers (`s`), where each integer is either 0 or 1. It calculates and prints the total count of 1s in the list, including the length of each segment of consecutive 1s.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, the input is a binary string s where 2 ≤ |s| ≤ 2⋅10^5 and s consists only of '0' and '1'.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t test cases have been processed.
#Overall this is what the function does:The function processes a specified number of test cases (t). For each test case, it reads a binary string (s) and counts the number of '1's in the string. After processing all test cases, it does not return any value but ensures that the count of '1's for each binary string is computed.

