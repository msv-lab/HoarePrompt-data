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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 100, alphabet is 'abcdefghijklmnopqrstuvwxyz', and for each iteration of the loop, n is an integer such that 3 ≤ n ≤ 78, with the final value of word determined by the conditions inside the loop.
#Overall this is what the function does:The function reads a series of test cases (t), each containing an integer (n) within the range 3 to 78. For each integer, it constructs a string (word) based on specific conditions and prints the result. The function does not return any value but produces output for each test case.

