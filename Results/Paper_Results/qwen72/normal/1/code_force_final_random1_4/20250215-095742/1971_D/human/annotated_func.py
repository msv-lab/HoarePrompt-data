#State of the program right berfore the function call: The function should take a single parameter `s` which is a binary string (a string consisting of characters '0' and '1') with a length of 1 to 500 characters.
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
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: After the loop executes all iterations, `s` is a new input string with any length greater than 1, `t` is 0 (since the loop has completed all iterations), `i` is `t-1` (which is the final value of `i` after the last iteration), `j` is `len(s) - 1` (indicating the loop has processed the entire string `s`), `count` is the number of adjacent pairs in `s` where the characters are different, and `flag` is True if there is at least one pair of adjacent characters in `s` where the first character is '0' and the second character is '1'. If `flag` is True, `count` is the number of adjacent pairs in `s` where the characters are different minus 1.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads a binary string `s`. It then calculates the number of adjacent character pairs in `s` that are different. If there is at least one pair where the first character is '0' and the second is '1', the count is decremented by 1. The function prints the final count for each test case. After processing all test cases, the function completes, and the final state is that `t` is 0, `i` is `t-1`, `j` is `len(s) - 1`, and `count` is the calculated value for the last test case.

