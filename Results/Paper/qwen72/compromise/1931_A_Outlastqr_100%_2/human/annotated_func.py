#State of the program right berfore the function call: The function should take an integer t as input, where 1 <= t <= 100, representing the number of test cases. For each test case, it should take an integer n, where 3 <= n <= 78, representing the encoded word.
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
        
    #State: Output State: The loop will print a series of encoded words based on the input values of `n` for each test case. The variable `i` will have iterated from 0 to `t-1`, and the variable `word` will be reset and recalculated for each iteration. The variable `n` will be the last input value for the final test case. The `alphabet` string remains unchanged as 'abcdefghijklmnopqrstuvwxyz'.
#Overall this is what the function does:The function `func` takes no parameters and does not return any value. It reads an integer `t` from the user, where 1 <= t <= 100, representing the number of test cases. For each test case, it reads another integer `n` from the user, where 3 <= n <= 78, and prints a decoded word based on the value of `n`. The decoded word is constructed as follows: if `n` > 52, the word is the `n-53`-th letter of the alphabet followed by 'zz'; if 27 < `n` <= 52, the word is 'a' followed by the `n-28`-th letter of the alphabet and 'z'; if `n` == 27, the word is 'aay'; otherwise, the word is 'aa' followed by the `n-3`-th letter of the alphabet. The variable `alphabet` remains unchanged as 'abcdefghijklmnopqrstuvwxyz'. After the function concludes, `t` test cases will have been processed, and the corresponding decoded words will have been printed.

