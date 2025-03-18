#State of the program right berfore the function call: The function `func` is expected to take no input parameters, but based on the problem description, it should be designed to handle multiple test cases, each with a string `s` of length at most 10 consisting of lowercase English letters. The function should be called in a loop or similar structure to process each test case.
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
        
    #State: The loop will have processed `n` test cases, where for each test case: if the string `s` consists of only one unique character, it will print 'NO'. Otherwise, it will print 'YES', followed by the lexicographically smallest or largest version of the string `s` depending on whether `s` is already sorted in ascending order or not. The variables `a`, `b`, and `c` will be updated for each iteration based on the current string `s`, but their values will not persist outside the loop.
#Overall this is what the function does:The function `func` processes multiple test cases, each with a string `s` of length at most 10 consisting of lowercase English letters. It reads the number of test cases `n` from the input, and for each test case, it reads a string `s`. If the string `s` consists of only one unique character, it prints 'NO'. Otherwise, it prints 'YES', followed by the lexicographically smallest version of the string if `s` is not already sorted in ascending order, or the lexicographically largest version of the string if `s` is already sorted in ascending order. The function does not return any values, and the variables `a`, `b`, and `c` are local to each iteration of the loop and do not persist outside of it.

