#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is a string of length 5 consisting of characters 'A' and 'B'. All t strings across all test cases are distinct.
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
        
    #State: Output State: The output state consists of `t` lines, each line containing either 'A' or 'B'. For each input string `s` of length 5 consisting of 'A' and 'B', if the number of 'A's is greater than the number of 'B's, the corresponding line contains 'A'; otherwise, it contains 'B'.
#Overall this is what the function does:The function processes an integer `t` (where 1 ≤ t ≤ 32) representing the number of test cases, followed by `t` strings, each of length 5 consisting of characters 'A' and 'B'. For each string, it counts the number of 'A's and 'B's. If the count of 'A's is greater than the count of 'B's, it prints 'A'; otherwise, it prints 'B'. After processing all strings, it outputs `t` lines, each containing either 'A' or 'B' based on the comparison.

