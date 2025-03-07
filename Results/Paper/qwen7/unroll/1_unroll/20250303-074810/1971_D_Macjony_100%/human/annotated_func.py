#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with a length between 1 and 500, inclusive.
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
        
    #State: Output State: `t` is an input integer between 1 and 500, and for each input string `s`, the variable `count` is calculated based on the rules inside the loop. If there is at least one occurrence where a '0' is immediately followed by a '1', `count` will be decremented by 1. The final value of `count` for each string `s` is printed.
#Overall this is what the function does:The function processes a series of test cases where each test case consists of an integer `t` and a binary string `s`. For each string `s`, it counts the number of consecutive character pairs where a '0' is immediately followed by a '1'. If such a pair exists, the count is decremented by 1. Finally, it prints the adjusted count for each string `s`.

