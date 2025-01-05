#State of the program right berfore the function call: l is an integer representing the length of the corridor (1 ≤ l ≤ 1000), p is an integer representing the speed of Harry's magic spell (1 ≤ p ≤ 500), and q is an integer representing the speed of You-Know-Who's magic spell (1 ≤ q ≤ 500).
def func():
    l = input()
    p = input()
    q = input()
    print(float(l) / (p + q)) * p
#Overall this is what the function does:The function accepts integer inputs `l`, `p`, and `q`, performs a calculation involving the lengths and speeds but does not return any results or indicate a winner between Harry and You-Know-Who.

