#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of the letters 'A' and 'B'.
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
        
    #State: Output State: The value of `t` remains unchanged, and for each string `s` provided according to the value of `t`, the output is either 'A' or 'B' based on whether the count of 'A's is greater than the count of 'B's in the string `s`. If the count of 'A's is greater, 'A' is printed; otherwise, 'B' is printed.
#Overall this is what the function does:The function processes a series of input strings, each of length 5 consisting of 'A' and 'B'. For each string, it counts the occurrences of 'A' and 'B'. If the count of 'A's is greater, it prints 'A'; otherwise, it prints 'B'. The function reads the number of such strings to process from the input and performs this operation for each string. After processing all strings, it outputs the result for each one.

