#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and s is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: `t` is an integer such that 1 <= t <= 1000, `s` is the last input string (a string of length at most 10 consisting of lowercase English letters), `_` is `t-1`, and `s2` is a shuffled version of the last input string `s`. If the last `s` is not equal to `s2`, the condition `s != s2` holds true. If the last `s` is equal to `s2`, the condition `s == s2` holds true.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 <= t <= 1000. For each test case, it reads a string `s` of lowercase English letters with a maximum length of 10. It then generates a random shuffle `s2` of the string `s`. If `s2` is different from `s`, it prints "Yes" followed by the shuffled string `s2`. If `s2` is the same as `s`, it prints "No". After processing all test cases, the function does not return any value, but the final state includes `t` being the original input integer, `s` being the last input string, and `_` being `t-1`.

