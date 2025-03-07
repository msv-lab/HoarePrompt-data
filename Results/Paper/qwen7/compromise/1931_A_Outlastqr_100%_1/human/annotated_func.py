#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100, alphabet is a string containing all lowercase letters from 'a' to 'z', and n is an integer such that 1 ≤ n ≤ 78. After the loop executes all iterations, the value of `word` depends on the input values provided during each iteration of the loop. Each iteration sets `word` based on the value of `n`, and prints the result. The final state of `word` will be the last printed value after all iterations.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` (3 ≤ n ≤ 78). Based on the value of `n`, it constructs a string `word` using predefined rules and prints the result. After processing all test cases, the function does not return any value but prints the constructed strings `word` for each test case.

