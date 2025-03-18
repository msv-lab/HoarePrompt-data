#State of the program right berfore the function call: s is a list of integers where each integer is either 0 or 1, and the length of the list is at least 2.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: Output State: `s` is a list of integers where each integer is either 0 or 1, and the length of the list is at least 2, and `ans` is the sum of all segments of consecutive 1's in `s` plus the number of such segments, with `n` being reset to 0 at the start of each segment of 0's.
    print(ans)
    #This is printed: ans (where ans is the sum of all segments of consecutive 1's in s plus the number of such segments)
#Overall this is what the function does:The function accepts a list `s` of integers, where each integer is either 0 or 1, and the length of the list is at least 2. It calculates and prints the sum of all segments of consecutive 1's in `s` plus the number of such segments. After processing the list, it resets the count of consecutive 1's (`n`) to 0 and outputs the final result.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, a binary string s is provided on a new line with the length of the string satisfying 2 ≤ |s| ≤ 2 ⋅ 10^5.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t test cases have been processed.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it calls `func_1()` with a binary string `s`. After processing all test cases, it concludes without returning any value.

