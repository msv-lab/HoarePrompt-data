#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of the characters 'A' and 'B'.
def func():
    t = int(input())
    for i in range(t):
        a = input()
        
        l = 0
        
        h = 0
        
        for j in a:
            if j == 'A':
                l += 1
            else:
                h += 1
        
        if l > h:
            print('A')
        else:
            print('B')
        
    #State: Output State: The output state consists of the sequence of characters 'A' or 'B' printed during each iteration of the loop, depending on whether the count of 'A' is greater than the count of 'B' in the string `a`. For each input string `a`, if the number of 'A's is greater than the number of 'B's, 'A' is printed; otherwise, 'B' is printed.
#Overall this is what the function does:The function processes a series of input strings, each of length 5 consisting of 'A' and 'B'. It counts the occurrences of 'A' and 'B' in each string. Based on which character appears more frequently ('A' or 'B'), it prints either 'A' or 'B' for each string. The function does not return any value but outputs the result for each input string.

