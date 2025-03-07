#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of letters 'A' and 'B'.
def func():
    t = int(input())
    for q in range(t):
        ac = 0
        
        bc = 0
        
        s = input()
        
        for i in s:
            if i == 'A':
                ac += 1
            else:
                bc += 1
        
        if ac > bc:
            print('A')
        else:
            print('B')
        
    #State: Output State: The variable `t` retains its initial value as an integer between 1 and 32 inclusive. After all iterations of the loop, `q` will be equal to `t - 1`. For each iteration of the loop, `ac` and `bc` are updated based on the counts of 'A' and 'B' characters in the string `s` provided during that iteration. The final output of the loop will consist of `t` lines, each line containing either 'A' or 'B', depending on whether the count of 'A' characters was greater than the count of 'B' characters in the respective string `s`. The variable `s` is not relevant to the final output state since it is redefined as an empty string at the start of each iteration.
    #
    #In summary, after all iterations of the loop, the output will be a series of 'A' or 'B' characters, one per line, corresponding to the result of comparing the counts of 'A' and 'B' in each of the `t` strings processed.
#Overall this is what the function does:The function processes up to 32 input strings, each of length 5 consisting of 'A' and 'B'. For each string, it counts the occurrences of 'A' and 'B'. If the count of 'A' is greater than the count of 'B', it prints 'A'; otherwise, it prints 'B'. The function does not return any value but outputs 'A' or 'B' for each of the input strings.

