#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and each string s is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: The loop iterates through t inputs, and for each input string s, it generates a shuffled version s2. If s2 is different from s, it prints 'Yes' followed by s2. If s2 is the same as s, it prints 'No'. The value of t remains unchanged, and each s is processed independently, so no state variables are altered outside of the loop's scope.
#Overall this is what the function does:The function `func` processes a series of input strings. It first reads an integer `t` (1 <= t <= 1000) indicating the number of strings to process. For each of these strings, it generates a shuffled version `s2`. If `s2` is different from the original string `s`, it prints 'Yes' followed by `s2`. If `s2` is the same as `s`, it prints 'No'. The function does not return any value, and the value of `t` remains unchanged throughout the execution. Each string `s` is processed independently, and no state variables are altered outside the loop's scope.

