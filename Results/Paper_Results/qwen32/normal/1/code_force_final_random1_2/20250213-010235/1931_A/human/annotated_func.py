#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
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
        
    #State: The loop has executed `t` times, printing `t` words based on the respective `n` values provided for each iteration. The variable `i` is `t`, and the `alphabet` string remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads another integer `n`. It then generates and prints a specific string based on the value of `n` for each test case. The generated string is constructed using lowercase letters from the English alphabet according to predefined rules.

