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
        
    #State: A series of printed strings, each constructed based on the value of `n` read in each iteration of the loop. The format of each printed string depends on the value of `n`: if `n > 52`, the string is `alphabet[n - 53] + 'zz'`; if `26 < n <= 52`, the string is `'a' + alphabet[n - 28] + 'z'`; if `n <= 26`, the string is `'aa' + alphabet[n - 3]`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads an integer `n` (where 3 <= n <= 78). It then prints a string based on the value of `n`: if `n > 52`, it prints a string in the format `alphabet[n - 53] + 'zz'`; if `26 < n <= 52`, it prints a string in the format `'a' + alphabet[n - 28] + 'z'`; if `n <= 26`, it prints a string in the format `'aa' + alphabet[n - 3]`.

