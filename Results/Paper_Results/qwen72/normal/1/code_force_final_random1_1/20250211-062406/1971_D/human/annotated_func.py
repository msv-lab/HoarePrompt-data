#State of the program right berfore the function call: The function should take a single argument, `s`, which is a binary string (a string consisting of characters '0' and '1') with a length of 1 to 500 characters.
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
        
    #State: After all iterations of the loop, `s` is the last input string provided with a length greater than 1, `t` is the initial value provided, `i` is `t - 1`, `j` is `len(s) - 1`, `count` is the number of adjacent character pairs in `s` that are different. If `flag` is True, `count` is reduced by 1, indicating that at least one pair of adjacent characters in `s` consists of '0' followed by '1'. Otherwise, `flag` remains False, and `count` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, then for each test case, it reads a binary string `s`. It calculates the number of adjacent character pairs in `s` that are different, adjusting the count if a '0' is immediately followed by a '1'. The function prints the adjusted count for each test case. The final state of the program after the function concludes is that `t` test cases have been processed, and the adjusted counts have been printed for each input string `s`.

