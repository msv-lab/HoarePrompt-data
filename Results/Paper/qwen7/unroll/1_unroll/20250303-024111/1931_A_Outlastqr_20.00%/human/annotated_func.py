#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 100, alphabet is a string containing all lowercase letters from 'a' to 'z', and n is an integer such that 3 ≤ n ≤ 78 after all iterations of the loop. The value of `word` will vary based on the input values for `n` during each iteration, but it will always follow the rules defined within the loop body.
#Overall this is what the function does:The function reads a series of test cases, each containing an integer \( n \) (where \( 3 \leq n \leq 78 \)), and for each \( n \), it constructs a string \( word \) based on specific rules. It then prints each constructed string. After processing all test cases, the function does not return any value.

