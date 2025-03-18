#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
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
        
    #State: After the loop executes all its iterations, `i` will be equal to the total number of test cases (which is provided as input at the start), `n` will be an integer between 1 and 100 for each iteration, and `word` will be constructed based on the value of `n` according to the rules specified in the loop body.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer \( n \) (where \( 3 \leq n \leq 78 \)). For each \( n \), it constructs a string `word` based on specific rules and prints it. If \( n \) is greater than 52, `word` is formed by appending 'zz' to the character at position \( n - 53 \) in the lowercase alphabet. If \( n \) is greater than 26 but less than or equal to 52, `word` is formed by appending 'z' to the character at position \( n - 28 \) in the lowercase alphabet, and 'a' before it. Otherwise, `word` is formed by appending 'zz' to the character at position \( n - 3 \) in the lowercase alphabet, with 'aa' before it. The function does not return any value but prints the constructed string for each test case.

