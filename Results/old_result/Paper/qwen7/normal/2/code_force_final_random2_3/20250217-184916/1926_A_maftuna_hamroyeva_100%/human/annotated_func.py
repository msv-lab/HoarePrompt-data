#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of the characters 'A' and 'B'. All t strings across all test cases are distinct.
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
        
    #State: Output State: After the loop executes all iterations, `t` is an integer between 1 and 32, and for each iteration `i` from 0 to `t-1`, `a` is a string representing the input for that iteration, `l` is the total count of 'A' characters in `a`, and `h` is the count of all other characters in `a`. The final output of the program will be a sequence of 'A' or 'B' based on whether `l` (the count of 'A' characters) is greater than `h` (the count of non-'A' characters) for each string `a`. If `l` is greater than `h` for any string `a`, the corresponding output will be 'A'; otherwise, it will be 'B'.
    #
    #In summary, the final output state will consist of a series of 'A' or 'B' characters, one for each input string processed, determined by the comparison of the counts of 'A' and non-'A' characters in each string.
#Overall this is what the function does:The function processes an integer `t` where 1 ≤ t ≤ 32, and for each test case, an input string of length 5 consisting of the characters 'A' and 'B'. It counts the number of 'A' characters in each string and compares this count to the number of non-'A' characters. Based on this comparison, it prints 'A' if the count of 'A' characters is greater, otherwise it prints 'B'. The function returns nothing but outputs a sequence of 'A' or 'B' characters, one for each input string processed.

