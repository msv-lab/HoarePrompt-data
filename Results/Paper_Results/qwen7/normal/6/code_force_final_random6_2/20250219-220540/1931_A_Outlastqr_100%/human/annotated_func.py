#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: After all iterations of the loop have finished, `t` is a positive integer such that \(1 \leq t \leq 100\), `n` is the last integer entered by the user, `word` is either "zz", "aay", or "aaa", and `i` is 99 (since the loop runs `int(input())` times, and we assume the user inputs a value that allows the loop to run up to its maximum of 100 iterations).
#Overall this is what the function does:The function processes a series of test cases defined by the user. For each test case, it reads an integer \( n \) and generates a specific string based on the value of \( n \). If \( n \) is greater than 52, it appends "zz" to a string formed from the 53rd character of the alphabet. If \( n \) is between 28 and 52, it appends the 29th character of the alphabet followed by "z". If \( n \) is 27, it sets the string to "aay". If \( n \) is between 3 and 26, it appends "aa" followed by the \( n \)-th character of the alphabet. The function prints the generated string for each test case.

