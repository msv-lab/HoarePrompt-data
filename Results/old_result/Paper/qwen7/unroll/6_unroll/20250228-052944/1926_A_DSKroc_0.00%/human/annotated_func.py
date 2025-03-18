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
        
    #State: Output State: t is an integer between 1 and 32 inclusive, ac and bc are lists of integers where each pair (ac[i], bc[i]) represents the counts of 'A' and 'B' respectively in the i-th string input.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: t is an integer between 1 and 32 inclusive, ac and bc are lists of integers where each pair (ac[i], bc[i]) represents the counts of 'A' and 'B' respectively in the i-th string input. If the length of ac is greater than the length of bc, the length of ac remains greater than the length of bc. If the length of ac is equal to the length of bc, the length of ac remains equal to the length of bc.
#Overall this is what the function does:The function processes `t` input strings, each of length 5 consisting of 'A' and 'B'. It counts the occurrences of 'A' and 'B' in each string and prints 'A' if the count of 'A' is greater than the count of 'B' in any string, otherwise it prints 'B'. The function does not return any value but prints the result for each string.

