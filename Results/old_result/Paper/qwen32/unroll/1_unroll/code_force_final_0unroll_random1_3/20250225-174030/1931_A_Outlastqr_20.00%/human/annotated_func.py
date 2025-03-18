#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
def func():
    alphabet = string.ascii_lowercase
    for i in range(int(input())):
        n = int(input())
        
        word = ''
        
        if n > 52:
            word += alphabet[n - 53] + 'zz'
        elif n > 26:
            word += 'a' + alphabet[n - 28] + 'z'
        else:
            word += 'aa' + alphabet[n - 3]
        
        print(word)
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` is the value assigned in the last iteration (an integer such that 3 <= n <= 78), `alphabet` is 'abcdefghijklmnopqrstuvwxyz'
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n` where 3 <= n <= 78. For each test case, it generates and prints a specific string based on the value of `n`. The final state of the program is that it has printed a string for each of the `t` test cases.

