#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of the characters 'A' and 'B'. All t strings across all test cases are distinct.
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
        
    #State: Postcondition: `t` is the total number of iterations the loop will run, which is an integer between 1 and 32 inclusive. `q` ranges from 0 to `t-1` across all iterations. For each iteration, `ac` is the total count of 'A' characters in the input string `s`, and `bc` is the total count of characters in `s` that are not 'A'. After all iterations, if `ac` is greater than `bc` for any iteration, the condition `ac > bc` holds true for at least one iteration. Otherwise, `ac` is less than or equal to `bc` for all iterations.
#Overall this is what the function does:The function processes an integer `t` (where `1 ≤ t ≤ 32`) representing the number of test cases. For each test case, it reads a string `s` of length 5 consisting of 'A' and 'B'. It counts the occurrences of 'A' and 'B' in each string and prints 'A' if the count of 'A' is greater than the count of 'B', otherwise it prints 'B'. After processing all test cases, the function does not return anything.

