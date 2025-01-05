#State of the program right berfore the function call: c1, c2, c3, c4, and c5 are integers representing the number of coins that each of the five players has at the end of the game, where 0 ≤ c1, c2, c3, c4, c5 ≤ 100.
def func():
    c = map(int, raw_input().split())
    s = sum(c)
    print - 1 if s == 0 or s % len(c) != 0 else s / len(c)
#Overall this is what the function does:The function accepts no parameters, reads the number of coins for five players from input, and returns the average number of coins per player if the total is greater than zero and divisible by five; otherwise, it returns -1.

