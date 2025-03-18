#State of the program right berfore the function call: The function `func` is expected to take an integer `n` as input, where 3 ≤ n ≤ 78, representing the encoded sum of the positions of three lowercase Latin letters.
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
        
    #State: The loop has completed all iterations, and the final value of `i` is `input() - 1`. For each iteration, `n` was an input integer within the range 3 to 78, and `word` was printed based on the following rules: If `n` > 52, `word` contained the character from the `alphabet` string at index `n - 53` followed by 'zz'. If `n` was between 28 and 52 (inclusive), `word` contained 'a' followed by the character at index `n - 28` in the `alphabet` string, followed by 'z'. If `n` was 27, `word` was 'aay'. If `n` was between 3 and 26 (inclusive), `word` was 'aa' followed by the character at index `n - 3` in the `alphabet` string.
#Overall this is what the function does:The function `func` reads a series of integers from the user, where each integer `n` (3 ≤ n ≤ 78) represents the encoded sum of the positions of three lowercase Latin letters. For each integer `n`, the function prints a corresponding three-letter word based on the following rules: If `n` > 52, the word is the character at index `n - 53` in the alphabet followed by 'zz'. If `n` is between 28 and 52 (inclusive), the word is 'a' followed by the character at index `n - 28` in the alphabet, followed by 'z'. If `n` is 27, the word is 'aay'. If `n` is between 3 and 26 (inclusive), the word is 'aa' followed by the character at index `n - 3` in the alphabet. The function does not return any value but prints the resulting word for each input integer.

