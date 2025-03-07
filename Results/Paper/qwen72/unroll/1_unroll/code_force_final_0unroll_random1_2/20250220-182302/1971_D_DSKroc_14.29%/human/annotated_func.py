#State of the program right berfore the function call: The function should take a single argument, a string `s` consisting of characters \texttt{0} and \texttt{1}, where 1 \leq |s| \leq 500. The function is expected to handle multiple test cases, where the number of test cases `t` is an integer such that 1 \leq t \leq 500.
def func():
    t = int(input())
    for q in range(t):
        s = input()
        
        count = 0
        
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                count += 1
        
        print(count + 1)
        
    #State: The variable `t` remains unchanged, and the loop prints the number of positions in each string `s` where a character is greater than the character immediately following it, plus one, for each of the `t` test cases. The variable `s` will contain the last input string provided. The variable `count` will be the count of such positions for the last input string, plus one.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads a string `s` consisting of characters '0' and '1'. It then calculates the number of positions in `s` where a character is greater than the character immediately following it, and prints this count plus one. After processing all test cases, the function does not return any value, but the variable `t` remains unchanged, `s` contains the last input string, and `count` contains the last calculated count plus one.

