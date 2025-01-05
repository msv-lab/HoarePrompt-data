#State of the program right berfore the function call: c1, c2, c3, c4, and c5 are integers representing the number of coins each player has at the end of the game, where each ci (for i = 1 to 5) is in the range 0 ≤ ci ≤ 100.
def func():
    c = map(int, raw_input().split())
    s = sum(c)
    print - 1 if s == 0 or s % len(c) != 0 else s / len(c)
#Overall this is what the function does:The function accepts no parameters and reads five integers from input, representing the number of coins each player has. It calculates the total number of coins and checks if the total is zero or not evenly divisible by the number of players (five). If the total is zero or not divisible by five, the function prints -1; otherwise, it prints the average number of coins per player.

