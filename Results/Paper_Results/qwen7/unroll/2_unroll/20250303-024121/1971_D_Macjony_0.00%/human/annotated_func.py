#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string such that 1 ≤ |s| ≤ 500.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 500, and for each `i` in the range of `t`, `count` is the number of consecutive characters in the string `s` (input at the `i`-th iteration), minus one if the substring "01" appears anywhere in `s`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a binary string `s`. It counts the number of consecutive characters in `s`, subtracting one from the count if the substring "01" appears anywhere in `s`. The function then prints the adjusted count for each test case.

