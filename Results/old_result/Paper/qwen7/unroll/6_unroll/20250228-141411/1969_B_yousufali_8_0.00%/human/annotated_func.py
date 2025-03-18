#State of the program right berfore the function call: s is a list of integers where each integer is either 0 or 1.
def func_1():
    s = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 1:
            n += 1
        
        if s[i] == 0 and n != 0:
            ans += n + 1
        
    #State: Output State: `ans` is the count of consecutive 1's plus one for each segment of 0's in the list `s`. `n` is 0.
    print(ans)
    #This is printed: 1
#Overall this is what the function does:The function reads a list of integers (0s and 1s) from user input, counts the number of consecutive 1s and adds 1 for each segment of 0s in the list, and prints the total count.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, the input is a binary string s (2 ≤ |s| ≤ 2⋅10^5) representing the string that needs to be sorted in non-descending order using cyclic shifts.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t test cases have been processed.
#Overall this is what the function does:The function processes a specified number of test cases (`t`). For each test case, it takes a binary string `s` as input (with a length between 2 and 2⋅10^5), sorts the string in non-descending order using cyclic shifts, and does not return any value. After processing all test cases, the function concludes.

