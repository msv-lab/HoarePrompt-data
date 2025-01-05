#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5) representing the number of houses, and hi is a list of n positive integers (1 ≤ hi ≤ 10^9) representing the number of floors in each house.
def func():
    n = int(sys.stdin.next())
    floors = map(int, sys.stdin.next().split(' '))
    m = 0
    s = []
    for h in floors[::-1]:
        s.append('%i' % (m - h + 1 if m - h + 1 > 0 else 0))
        
        m = max(h, m)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer; `floors` is a map object containing at least 1 integer; `h` is the first element of `floors`; `s` is updated to contain values calculated as `m - h + 1` or `0` for each element in `floors`, in reverse order; `m` is assigned the maximum value from all elements in `floors`.
    print(' '.join(s[::-1]).strip())
#Overall this is what the function does:The function reads a positive integer `n` representing the number of houses and a list of `n` positive integers indicating the number of floors in each house. It calculates the difference between the maximum floors encountered so far and the current number of floors, ensuring that it does not return negative values. The results are printed in the order corresponding to the original input of floors. The function does not handle cases where the input might be invalid or where `n` is 0, as it assumes valid input is always provided.

