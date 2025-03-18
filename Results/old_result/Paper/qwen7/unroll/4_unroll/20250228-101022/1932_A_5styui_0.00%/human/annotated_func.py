#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of input is a string of length n consisting of '.', '@', and '*', where '.' represents an empty cell, '@' represents a cell with a coin, and '*' represents a cell with thorns. Additionally, the first cell is guaranteed to be empty ('.') and the string does not contain consecutive '*'s.
def func():
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 1000, `a` is an input integer between 1 and 50 inclusive, `s` is 0.
    #
    #Explanation: The loop processes each value of `i` from 0 to `a-1`. For each iteration, it reads an integer `d` and a string `b`. It then iterates through each character of `b`, counting occurrences of the '@' character and breaking out of the inner loop under certain conditions. After processing `b`, it prints the count of '@' characters and resets `s` to 0 for the next iteration. Since `s` is reset to 0 at the end of each iteration, the final value of `s` will always be 0 regardless of the input. Therefore, the output state remains the same as the initial state for `s`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `d` followed by a string `b` of length up to 50, containing characters '.', '@', and '*'. It counts the number of '@' characters in the string `b`, ignoring any string that contains consecutive '*'s. If the string does not contain consecutive '*'s and starts with '.', it prints the count of '@' characters and resets the count to 0 for the next test case. The final output for each test case is the count of '@' characters found in the string `b`.

