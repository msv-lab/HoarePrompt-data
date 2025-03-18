#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string consists of exactly 5 characters where each character is either 'A' or 'B'.
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
        
    #State: Output State: `t` is the number of strings processed, `ac` is the total count of 'A' characters across all strings, `bc` is the total count of non-'A' characters across all strings.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: Postcondition: `t` is the number of strings processed, `ac` is the total count of 'A' characters across all strings, `bc` is the total count of non-'A' characters across all strings. If `ac` is greater than `bc`, the condition remains unchanged. If `ac` is less than or equal to `bc`, the condition also remains unchanged.
#Overall this is what the function does:The function processes a specified number of input strings, each consisting of 5 characters ('A' or 'B'), and counts the occurrences of 'A' and 'B'. After processing all strings, it prints 'A' if the total count of 'A' characters is greater than the count of 'B' characters; otherwise, it prints 'B'. The function does not return any value but modifies the output based on the comparison between the counts of 'A' and 'B' characters across all input strings.

