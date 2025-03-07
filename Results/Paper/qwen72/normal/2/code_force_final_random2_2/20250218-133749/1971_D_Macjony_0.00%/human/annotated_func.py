#State of the program right berfore the function call: The function `func` is expected to process multiple test cases, where each test case includes a binary string `s` (1 ≤ |s| ≤ 500) consisting of characters '0' and '1'. The number of test cases `t` is a positive integer (1 ≤ t ≤ 500).
def func():
    t = int(input())
    for i in range(t):
        s = input()
        
        count = 1
        
        flag = False
        
        j = 0
        
        while j < len(s) - 1:
            if s[j] != s[j + 1]:
                count += 1
                if s[j] == '0' and s[j + 1] == '1':
                    flag = True
                    j += 1
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: `t` is greater than or equal to 1, `i` is `t - 1`, `s` is the last input string with a length greater than 1, `j` is `len(s) - 1`, `count` is the number of transitions between different characters in the string `s` minus 1 if `flag` is True, otherwise `count` is the number of transitions between different characters in the string `s`. `flag` is True if there is at least one occurrence of '0' followed by '1' in `s`.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` indicating the number of test cases, and for each test case, it reads a binary string `s`. The function calculates the number of transitions between different characters in the string `s` and subtracts 1 if there is at least one occurrence of '0' followed by '1'. The result for each test case is printed to the console. After processing all test cases, the function completes, and the final state is that `t` test cases have been processed, and the results for each test case have been printed.

