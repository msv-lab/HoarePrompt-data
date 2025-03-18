#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B'.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        first_black = s.find('B')
        
        last_black = s.rfind('B')
        
        min_paint = last_black - first_black + 1
        
        print(min_paint)
        
    #State: After all iterations of the loop have finished, `t` will be 0, as it starts as an input integer between 1 and \(10^4\) (inclusive) and is decremented by 1 in each iteration of the loop. For each iteration, `n` will be an input integer, `s` will be an input string, `first_black` will be the index of the first occurrence of 'B' in `s`, or -1 if 'B' is not found; `last_black` will be the index of the last occurrence of 'B' in `s`, or -1 if 'B' is not found; `min_paint` will be `last_black - first_black + 1`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a string `s` consisting of 'W' and 'B' characters, finds the first and last positions of 'B' in `s`, calculates the minimum number of consecutive 'B' characters between these positions, and prints this value. After processing all test cases, the variable `t` is set to 0.

