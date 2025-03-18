#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, n is an integer such that 3 <= n <= 78.
def func():
    alphabet = string.ascii_lowercase
    for i in range(int(input())):
        n = int(input())
        
        word = ''
        
        if n > 52:
            word += alphabet[n - 53] + 'zz'
        elif n > 27:
            word += 'a' + alphabet[n - 28] + 'z'
        elif n == 27:
            word = 'aay'
        else:
            word += 'aa' + alphabet[n - 3]
        
        print(word)
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` is an integer read from input such that 3 <= n <= 78, `alphabet` is a string containing all lowercase letters from 'a' to 'z', `i` is equal to `t` (indicating the loop has finished all iterations). For each iteration, `word` is a string updated based on the value of `n` as described: if `n` > 52, `word` is `alphabet[n - 53] + 'zz'`. If 28 <= `n` <= 52, `word` is `'a' + alphabet[n - 28] + 'z'`. If `n` is 27, `word` is `'aay'`. If 3 <= `n` <= 26, `word` is `'aa' + alphabet[n - 3]`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` such that 3 <= n <= 78 and prints a specific string based on the value of `n`. The printed string is determined by the following rules: if `n` > 52, the string is the letter at index `n - 53` in the alphabet followed by 'zz'; if 28 <= `n` <= 52, the string is 'a' followed by the letter at index `n - 28` in the alphabet and ending with 'z'; if `n` is 27, the string is 'aay'; if 3 <= `n` <= 26, the string is 'aa' followed by the letter at index `n - 3` in the alphabet.

