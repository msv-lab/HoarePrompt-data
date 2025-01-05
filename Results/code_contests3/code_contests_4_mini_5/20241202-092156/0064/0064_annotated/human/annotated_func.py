#State of the program right berfore the function call: c1, c2, c3, c4, and c5 are integers representing the number of coins each of the five players has at the end of the game, where 0 ≤ c1, c2, c3, c4, c5 ≤ 100.
def func():
    c = map(int, raw_input().split())
    s = sum(c)
    print - 1 if s == 0 or s % len(c) != 0 else s / len(c)
#Overall this is what the function does:The function accepts no parameters and reads five integers representing the number of coins each of five players has. It calculates the total number of coins and checks two conditions: if the total is zero (indicating all players are bankrupt) or if the total is not evenly divisible by five. If either condition is true, it prints -1; otherwise, it prints the average number of coins per player. The function does not identify the player with the highest number of coins, contrary to what the annotations suggest.

