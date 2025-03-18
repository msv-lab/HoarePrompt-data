#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each of the t test cases contains a string s of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        if len(s) == 1:
            print('No')
        elif len(set(s)) == 1 and len(s) > 1:
            print('No')
        else:
            s2 = ''.join(random.sample(s, len(s)))
            if s == s2:
                s2 = s[1:] + s[0]
            print('Yes')
            print(s2)
        
    #State: t is an integer such that 1 <= t <= 1000. Each of the t test cases has been processed, and for each test case, if the string s had a length of 1 or all characters were the same, "No" was printed. Otherwise, "Yes" was printed followed by a shuffled version of s (or a modified version if the shuffle resulted in the same string). The variable s is undefined or reset for each iteration, and the loop has completed all t iterations.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t` (1 <= t <= 1000), where each test case includes a string `s` of length at most 10 consisting of lowercase English letters. For each test case, if the string `s` has a length of 1 or all characters in `s` are the same, it prints "No". Otherwise, it prints "Yes" followed by a shuffled version of `s` (or a modified version if the shuffle resulted in the same string). After processing all `t` test cases, the function completes and the variable `s` is undefined or reset for each iteration.

