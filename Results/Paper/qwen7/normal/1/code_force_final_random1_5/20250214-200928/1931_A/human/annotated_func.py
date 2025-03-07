#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: The loop has completed all its iterations, and the final state of the program includes `i` being equal to the number of iterations specified by `int(input())`, `n` being the last input integer provided within the loop, and `word` being either 'zzzzzz', 'az', or 'aaa' based on the value of `n`.
#Overall this is what the function does:The function reads an integer `t` and then iterates `t` times. During each iteration, it reads another integer `n` and constructs a string `word` based on the value of `n`. If `n` is greater than 52, `word` is set to `'zz'` plus a character derived from the alphabet. If `n` is between 27 and 52, `word` is set to `'a'` plus a character derived from the alphabet plus `'z'`. If `n` is between 4 and 26, `word` is set to `'aa'` plus a character derived from the alphabet. After processing all inputs, the function prints the constructed string `word` for each iteration.

