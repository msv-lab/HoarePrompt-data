#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each of the t test cases, there is a string of length 5 consisting of the characters 'A' and 'B'. All t strings are distinct.
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
        
    #State: - `t` remains the same as the initial input.
    #- `q` will be equal to `t` after the loop finishes, as it will have incremented from 0 to `t-1`.
    #- `s` will be the string from the last test case.
    #- `ac` and `bc` will be the counts of 'A' and non-'A' characters, respectively, in the last test case's string.
    #
    #So, the final output state in the required format is:
    #
    #Output State:
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: `t` remains the same as the initial input. `q` will be equal to `t` after the loop finishes, as it will have incremented from 0 to `t-1`. `s` will be the string from the last test case. `ac` and `bc` will be the counts of 'A' and non-'A' characters, respectively, in the last test case's string. If `ac` is greater than `bc`, then `ac` is greater than `bc`. Otherwise, `ac` is less than or equal to `bc`.
#Overall this is what the function does:The function reads an integer `t` and `t` distinct strings of length 5 consisting of 'A' and 'B'. For each string, it counts the occurrences of 'A' and 'B'. After processing all strings, it prints 'A' if the last string has more 'A's than 'B's, otherwise it prints 'B'.

