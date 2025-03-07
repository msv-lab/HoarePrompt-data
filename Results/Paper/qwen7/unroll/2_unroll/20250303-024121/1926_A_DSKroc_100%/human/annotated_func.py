#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of the letters 'A' and 'B'. All t strings across all test cases are distinct.
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
        
    #State: Output State: `t` is an integer between 1 and 32 inclusive. For each input string `s` provided in the range of `t`, the output is either 'A' or 'B' based on whether the number of 'A's is greater than the number of 'B's in the string. If the number of 'A's is greater, 'A' is printed; otherwise, 'B' is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (1 ≤ t ≤ 32) and a string of length 5 containing 'A' and 'B'. For each test case, it counts the occurrences of 'A' and 'B' in the string. If the count of 'A' is greater than the count of 'B', it prints 'A'; otherwise, it prints 'B'. The function does not return any value but prints the result for each test case.

