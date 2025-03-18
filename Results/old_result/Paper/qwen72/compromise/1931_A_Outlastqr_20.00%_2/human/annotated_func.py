#State of the program right berfore the function call: The function `func` is expected to take an integer `n` as input, where 3 ≤ n ≤ 78, representing the encoded value of a three-letter word.
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
        
    #State: The loop prints a series of three-letter words based on the input values of `n` for each iteration. The `word` variable is reset to an empty string at the beginning of each iteration, and the final state of `word` after the loop finishes is an empty string. The `alphabet` variable remains unchanged as 'abcdefghijklmnopqrstuvwxyz'.
#Overall this is what the function does:The function `func` does not return any value but prints a series of three-letter words to the console. It reads an integer from the user, which specifies the number of iterations, and for each iteration, it reads another integer `n` (3 ≤ n ≤ 78). Based on the value of `n`, it constructs and prints a three-letter word. If `n` is greater than 52, the word is formed by appending 'zz' to the `n - 53`-th letter of the alphabet. If `n` is between 27 and 52, the word is formed by appending 'z' to the `n - 28`-th letter of the alphabet, with 'a' as the first letter. If `n` is between 3 and 26, the word is formed by appending the `n - 3`-th letter of the alphabet, with 'aa' as the first two letters. After the loop completes, the `word` variable is reset to an empty string for each iteration, and the `alphabet` variable remains unchanged.

