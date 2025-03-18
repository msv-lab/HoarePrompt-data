#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10 000 000) representing the amount of money, a is a positive integer (1 ≤ a ≤ 10 000 000) representing the cost of one bottle of Ber-Cola, and b is a positive integer (1 ≤ b ≤ 10 000 000) representing the cost of one Bars bar, where Vasya can buy x bottles of Ber-Cola and y Bars bars such that x·a + y·b = n, and x and y are non-negative integers.
def func_1():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        if (n - x * a) % b == 0:
            y = (n - x * a) // b
            print('YES')
            print(x, y)
            return
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `b` is an input integer, `a` is a non-zero input integer, `n` is greater than or equal to `-a`, and either the loop completed without finding a solution (in which case `x` is `n // a`) or the loop found a solution and returned (in which case the final values of `x` and `y` are the solution values).
    print('NO')
#Overall this is what the function does:The function determines whether it's possible to spend a given amount of money on two items with specific costs, and if so, finds the number of each item that can be bought. It accepts three implicit parameters: the amount of money and the costs of two items, all positive integers. The function then attempts to find non-negative integer values of x and y such that x times the cost of the first item plus y times the cost of the second item equals the given amount of money. If such values are found, it prints "YES" followed by the values of x and y, and returns None. If no such values are found after checking all possible combinations, it prints "NO" and returns None. The function handles cases where the amount of money is not enough to buy at least one item, as well as cases where the costs of the items are such that no combination can sum up to the given amount of money, by printing "NO" in such scenarios.

