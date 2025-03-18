#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and each string s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: The values of `t` and `n` remain unchanged. The variable `s` will be the last string input by the user during the loop execution. The variable `a` will be a set containing the unique characters of the last string `s`. The variable `b` will be the last string `s` sorted in ascending order. The variable `c` will be the last string `s` sorted in descending order.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, indicating the number of strings to process. For each of the `n` strings, it checks if the string consists of a single unique character. If so, it prints 'NO'. If the string has more than one unique character, it prints 'YES', followed by the string sorted in ascending order if it is not already sorted in ascending order, or the string sorted in descending order if it is sorted in ascending order. The function does not return any value. After the function concludes, the values of `t` and `n` remain unchanged, and the variables `s`, `a`, `b`, and `c` will hold the state of the last processed string: `s` will be the last string input, `a` will be a set of its unique characters, `b` will be the last string sorted in ascending order, and `c` will be the last string sorted in descending order.

