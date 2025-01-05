#State of the program right berfore the function call: l is an integer representing the length of the corridor (1 ≤ l ≤ 1000), p is an integer representing the speed of Harry's spell (1 ≤ p ≤ 500), and q is an integer representing the speed of You-Know-Who's spell (1 ≤ q ≤ 500).
def func():
    l = input()
    p = input()
    q = input()
    print(float(l) / (p + q)) * p
#Overall this is what the function does:The function accepts integer inputs representing the length of the corridor (l), the speed of Harry's spell (p), and the speed of You-Know-Who's spell (q). It calculates the time taken for Harry's spell to reach the end of the corridor based on the combined speeds of both spells and incorrectly attempts to print the result by multiplying the time by p, but it does not return any value. Additionally, the function does not handle input validation or edge cases where the inputs might not be integers or fall outside the specified ranges.

