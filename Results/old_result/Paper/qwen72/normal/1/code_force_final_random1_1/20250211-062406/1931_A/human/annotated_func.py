#State of the program right berfore the function call: The function should take an integer n as input, where 3 ≤ n ≤ 78, representing the encoded value of a three-letter word.
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
        
    #State: After the loop has executed all iterations, `i` will be equal to the input integer minus 1, `n` will be the last input integer provided, and `word` will be a string. The value of `word` will depend on the last input integer `n`: If `n` is between 53 and 78 (inclusive), `word` will be the character from the alphabet corresponding to the position `n - 53` followed by 'zz'. If `n` is between 27 and 52 (inclusive), `word` will be 'a' + the character at position `n - 28` in the alphabet + 'z'. If `n` is between 3 and 26 (inclusive), `word` will be 'aa' followed by the character at position `n - 3` in the alphabet.
#Overall this is what the function does:The function `func` reads multiple integers from the user, each representing an encoded value of a three-letter word. For each integer `n` (where 3 ≤ n ≤ 78), it generates and prints a corresponding three-letter word based on the following rules: If `n` is between 53 and 78 (inclusive), the word is the character from the alphabet corresponding to the position `n - 53` followed by 'zz'. If `n` is between 27 and 52 (inclusive), the word is 'a' followed by the character at position `n - 28` in the alphabet, followed by 'z'. If `n` is between 3 and 26 (inclusive), the word is 'aa' followed by the character at position `n - 3` in the alphabet. The function does not return any value; it only prints the generated words.

