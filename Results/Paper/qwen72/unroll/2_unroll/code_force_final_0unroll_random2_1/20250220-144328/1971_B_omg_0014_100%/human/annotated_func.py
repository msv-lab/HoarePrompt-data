#State of the program right berfore the function call: The function should take a single argument, `s`, which is a string of length at most 10 consisting of lowercase English letters. Additionally, the function should be able to handle multiple test cases, indicated by an integer `t` where 1 ≤ t ≤ 1000.
def func():
    n = int(input())
    for i in range(n):
        s = input()
        
        a = set(s)
        
        if len(a) == 1:
            print('NO')
        else:
            print('YES')
            b = ''.join(sorted(s))
            c = ''.join(sorted(s, reverse=True))
            if b == s:
                print(c)
            else:
                print(b)
        
    #State: The loop will execute `n` times, and for each iteration, it will read a string `s` from the input. If the string `s` consists of only one unique character, it will print 'NO'. If the string `s` has more than one unique character, it will print 'YES', followed by the lexicographically smallest or largest sorted version of `s` depending on the initial order of `s`. The variables `a`, `b`, and `c` will be redefined in each iteration, but their final values after the loop will depend on the last input string `s`. The variable `s` will hold the last input string read. The variable `n` will remain unchanged.
#Overall this is what the function does:The function reads an integer `n` from the input, representing the number of test cases. For each test case, it reads a string `s` from the input. If the string `s` consists of only one unique character, it prints 'NO'. If the string `s` has more than one unique character, it prints 'YES', followed by either the lexicographically smallest or largest sorted version of `s` depending on whether `s` is already in lexicographically smallest order. The function does not return any values; it only prints the results to the console. After the function concludes, the variable `n` remains unchanged, and `s` holds the last input string read.

