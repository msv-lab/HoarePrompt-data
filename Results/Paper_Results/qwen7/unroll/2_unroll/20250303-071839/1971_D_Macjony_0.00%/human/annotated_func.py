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
        
    #State: Output State: `t` is an integer such that 1 ≤ `t` ≤ 500, and for each `i` in the range of `t`, `count` is an integer representing the number of consecutive characters in the string `s` (input at the `i`-th iteration), adjusted by subtracting 1 if the substring "01" appears anywhere in `s`.
#Overall this is what the function does:The function processes an integer `t` and `t` binary strings `s`, each with a length between 1 and 500. For each string `s`, it counts the number of consecutive characters and adjusts this count by subtracting 1 if the substring "01" appears anywhere in `s`. The function prints the adjusted count for each string `s`.

