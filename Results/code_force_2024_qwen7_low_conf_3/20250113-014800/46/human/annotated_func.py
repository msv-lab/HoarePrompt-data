#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 32, and for each test case, the input string is of length 5 consisting only of the characters 'A' and 'B'.
def func():
    t = int(input())
    for _ in range(t):
        ab = [x for x in input()]
        
        n = len(ab)
        
        a = 0
        
        b = 0
        
        for i in range(n):
            if ab[i] == 'A':
                a += 1
            else:
                b += 1
        
        if a > b:
            print('A')
        else:
            print('B')
        
    #State of the program after the  for loop has been executed: `t` is 0, `ab` is the final list of characters from the last input string, `n` is the length of `ab`, `a` is the count of 'A' characters in `ab`, `b` is the count of 'B' characters in `ab`. If `a > b`, the message 'A' has been printed to the console for the last iteration. Otherwise, the message 'B' has been printed to the console for the last iteration.
#Overall this is what the function does:The function processes `t` input strings, each of length 5 consisting only of the characters 'A' and 'B'. For each input string, it counts the number of 'A' and 'B' characters. After processing all strings, it prints 'A' if the total count of 'A' characters is greater than the total count of 'B' characters; otherwise, it prints 'B'. The function does not return any value. It handles the case where `t` is between 1 and 32 inclusive.

