#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string consists of exactly 5 characters where each character is either 'A' or 'B'.
def func():
    t = int(input())
    for i in range(t):
        a = input()
        
        l = 0
        
        h = 0
        
        for j in a:
            if j == 'A':
                l += 1
            else:
                h += 1
        
        if l > h:
            print('A')
        else:
            print('B')
        
    #State: After the loop executes all iterations, `a` remains as the original input string, `j` is undefined, `l` contains the total number of 'A' characters in `a`, `h` contains the total number of non-'A' characters in `a`, and `i` is incremented by the length of `a` for each iteration of the loop. The condition either `l > h` or `l <= h` holds true based on the execution path taken.
#Overall this is what the function does:The function processes an input integer `t` representing the number of test cases, followed by `t` strings, each consisting of exactly 5 characters ('A' or 'B'). For each string, it counts the number of 'A' characters and the number of 'B' or 'C' characters (since 'C' is not a valid character, it is treated as 'B'). It then prints 'A' if the count of 'A' characters is greater than the count of 'B' characters, and 'B' otherwise. The function does not return any value.

