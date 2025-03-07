#State of the program right berfore the function call: The function `func` is expected to take no input parameters, but based on the problem description, it should be modified to take a string `s` as input, where `s` is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        if len(s) == 1:
            print('No')
        elif len(set(s)) == 1 and len(s) > 1:
            print('No')
        else:
            s2 = ''.join(random.sample(s, len(s)))
            if s == s2:
                s2 = s[1:] + s[0]
            print('Yes')
            print(s2)
        
    #State: The loop will execute a number of times equal to the integer provided by the user. For each iteration, the user will input a string `s`. If the string `s` has a length of 1 or all characters in the string are the same (and the length is greater than 1), the loop will print 'No'. Otherwise, it will print 'Yes' followed by a shuffled version of the string `s` (or a modified version if the shuffled string happens to be the same as the original). The variable `s` will be updated with each new input string in each iteration, but will not retain any value after the loop completes.
#Overall this is what the function does:The function `func` takes no input parameters but reads input from the user. It processes a series of strings provided by the user, where each string `s` is of length at most 10 and consists of lowercase English letters. For each string, if the string has a length of 1 or all characters in the string are the same, it prints 'No'. Otherwise, it prints 'Yes' followed by a shuffled version of the string `s` (or a modified version if the shuffled string is the same as the original). The function does not return any value. After the function concludes, the program state is such that all input strings have been processed, and the final output is a series of 'No' or 'Yes' followed by a shuffled string for each input.

