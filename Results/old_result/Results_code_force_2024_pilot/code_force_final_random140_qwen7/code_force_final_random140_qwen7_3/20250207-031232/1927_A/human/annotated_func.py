#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where at least one character is 'B'.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        first_black = s.find('B')
        
        last_black = s.rfind('B')
        
        min_paint = last_black - first_black + 1
        
        print(min_paint)
        
    #State: t is 3, n is an input integer, s is a new string input by the user, first_black is the index of the first occurrence of 'B' in s, last_black is the index of the last occurrence of 'B' in s, and min_paint is the difference between last_black and first_black plus one.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads a positive integer \( t \) (number of test cases), followed by \( t \) pairs of integers \( n \) and strings \( s \). For each string \( s \), which consists of 'W' and 'B' characters with at least one 'B', it finds the indices of the first and last 'B' characters, calculates the minimum number of wall paints needed to cover all 'B' characters, and prints this value. After processing all test cases, the function concludes without returning any value.

