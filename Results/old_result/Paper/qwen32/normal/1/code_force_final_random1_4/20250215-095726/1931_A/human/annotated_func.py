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
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` is the integer value of the user input from the last iteration, `alphabet` is the string 'abcdefghijklmnopqrstuvwxyz', `i` is equal to `t`. The loop has printed `t` lines, each containing the constructed `word` based on the respective `n` value from each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads another integer `n` (where 3 <= n <= 78). It then constructs and prints a specific string based on the value of `n`. The final state of the program is that it has processed all `t` test cases and printed the corresponding strings.

