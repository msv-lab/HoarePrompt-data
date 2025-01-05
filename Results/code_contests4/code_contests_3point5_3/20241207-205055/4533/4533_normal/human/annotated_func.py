#State of the program right berfore the function call: n is a positive integer representing the number of houses in the capital of Berland. hi is a list of positive integers where each element represents the number of floors in each house.**
def func():
    n = int(sys.stdin.next())
    floors = map(int, sys.stdin.next().split(' '))
    m = 0
    s = []
    for h in floors[::-1]:
        s.append('%i' % (m - h + 1 if m - h + 1 > 0 else 0))
        
        m = max(h, m)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `hi` is a list of positive integers representing the number of floors in each house, `m` is the maximum number of floors among all houses, `s` is a list containing the calculated values based on the formula provided in the loop
    print(' '.join(s[::-1]).strip())
#Overall this is what the function does:The function `func` reads input from the standard input, processes information about the number of houses in the capital of Berland and the number of floors in each house. It calculates and prints the values based on certain conditions. The function does not accept any parameters and operates solely on the input received.

