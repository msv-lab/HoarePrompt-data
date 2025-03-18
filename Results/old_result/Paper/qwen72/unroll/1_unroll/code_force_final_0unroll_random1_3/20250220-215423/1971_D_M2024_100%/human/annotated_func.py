#State of the program right berfore the function call: The function should take a single argument, a string `s` consisting of characters '0' and '1' where 1 <= |s| <= 500, and return an integer representing the minimum number of pieces needed to rearrange the string into a sorted binary string. Additionally, the function should handle multiple test cases, where the number of test cases `t` is an integer such that 1 <= t <= 500.
def func():
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut0 = 0
        
        cut1 = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut1 += 1
            if a[i] == '0' and a[i + 1] == '1':
                cut0 += 1
        
        if cut0 == 0:
            print(cut1 + 1)
        else:
            print(cut0 + cut1)
        
    #State: The value of `t` is unchanged, and `s` remains the same string consisting of characters '0' and '1'. The loop prints a number for each iteration based on the input string `a` provided during each iteration.
#Overall this is what the function does:The function reads an integer `t` from the input, representing the number of test cases. For each test case, it reads a string `a` consisting of characters '0' and '1' (1 <= |a| <= 500). The function calculates and prints the minimum number of pieces needed to rearrange the string `a` into a sorted binary string. The function does not return any value; instead, it prints the result for each test case. After the function concludes, the value of `t` is unchanged, and the input strings `a` remain the same.

