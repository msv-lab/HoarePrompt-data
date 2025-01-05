#State of the program right berfore the function call: c1, c2, c3, c4, and c5 are integers representing the number of coins each of the five players has at the end of the game, where 0 ≤ c1, c2, c3, c4, c5 ≤ 100.
def func():
    c = map(int, raw_input().split())
    s = sum(c)
    print - 1 if s == 0 or s % len(c) != 0 else s / len(c)
#Overall this is what the function does:The function accepts input representing the number of coins each of five players has, calculates the total number of coins, and returns -1 if the total is zero or if the total is not evenly divisible by the number of players (which is always 5). If the total is divisible by 5, it returns the average number of coins per player. The function does not explicitly limit the number of players to five, as described in the annotations, but it assumes the input will always correspond to five players based on the context.

