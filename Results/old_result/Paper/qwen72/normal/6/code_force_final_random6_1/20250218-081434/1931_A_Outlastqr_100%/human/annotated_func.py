#State of the program right berfore the function call: The function should accept an integer t (1 ≤ t ≤ 100) as the number of test cases, and for each test case, an integer n (3 ≤ n ≤ 78) representing the encoded word.
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
        
    #State: `t` is 0, `i` is `t - 1`, and `n` is an input integer for each test case. For each test case, if `n` > 52, `word` is the character at index `n - 53` in the `alphabet` string followed by 'zz'. If `n` > 27 and `n` <= 52, `word` is the string 'a' + `alphabet[n - 28]` + 'z'. If `n` is 27, `word` is 'aay'. If `n` is between 3 and 26 (inclusive), `word` is 'aa' followed by the character at index `n - 3` in the string `alphabet`.
#Overall this is what the function does:The function processes a number of test cases `t` (1 ≤ t ≤ 100). For each test case, it accepts an integer `n` (3 ≤ n ≤ 78) representing an encoded word. It prints a decoded word for each test case based on the value of `n`. If `n` > 52, the word is the character at index `n - 53` in the `alphabet` string followed by 'zz'. If `n` > 27 and `n` ≤ 52, the word is the string 'a' + the character at index `n - 28` in the `alphabet` string + 'z'. If `n` is 27, the word is 'aay'. If `n` is between 3 and 26 (inclusive), the word is 'aa' followed by the character at index `n - 3` in the `alphabet` string. The function does not return any value; it only prints the decoded words.

