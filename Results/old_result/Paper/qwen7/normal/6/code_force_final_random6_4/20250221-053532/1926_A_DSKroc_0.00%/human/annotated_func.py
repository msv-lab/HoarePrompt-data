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
        
    #State: Output State: All characters in the string `s` have been iterated over `t` times, `ac` is the total count of 'A' characters in `s`, and `bc` is the total count of non-'A' characters in `s`. The variable `q` ranges from 0 to `t-1` after all iterations, and `s` is the original input string without any modifications. `i` is irrelevant since the loop has completed.
    #
    #In simpler terms, after the loop has executed all its iterations, `ac` will hold the total number of 'A' characters in the input string `s`, `bc` will hold the total number of non-'A' characters in `s`, `q` will range from 0 to `t-1` (where `t` is the initial input), and `s` will remain unchanged as no modifications were made to it within the loop.
    if (ac > bc) :
        print('A')
        #This is printed: 'A'
    else :
        print('B')
        #This is printed: 'B'
    #State: All characters in the string `s` have been iterated over `t` times, `ac` is the total count of 'A' characters in `s`, and `bc` is the total count of non-'A' characters in `s`. The variable `q` ranges from 0 to `t-1` after all iterations, and `s` remains unchanged. Furthermore, if `ac` is greater than `bc`, the condition holds true; otherwise, `ac` is less than or equal to `bc`.
#Overall this is what the function does:The function processes an integer `t` (1 ≤ t ≤ 32) and an input string `s` of length 5 consisting of 'A' and 'B'. It counts the occurrences of 'A' and 'B' in the string `s`. After processing, it prints 'A' if the count of 'A' is greater than the count of 'B', and prints 'B' otherwise. The function does not modify the input string `s` and returns nothing.

