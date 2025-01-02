#State of the program right berfore the function call: x and y are non-negative integers.
def func_1(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` is the GCD of the original values of `x` and `y`, `y` is 0.
    return x
    #The program returns the GCD of the original values of `x` and `y`
#Overall this is what the function does:The function `func_1` accepts two parameters `x` and `y`, which are expected to be non-negative integers. It computes and returns the Greatest Common Divisor (GCD) of the original values of `x` and `y`. After the function concludes, `x` holds the GCD of the original `x` and `y`, and `y` is 0. The function handles the case where either `x` or `y` is 0 by returning the non-zero value as the GCD, and it correctly handles the case where both `x` and `y` are 0 by returning 0.

#State of the program right berfore the function call: n and m are integers such that 2 ≤ n ≤ 5000 and 1 ≤ m ≤ 20000. station is a list of n empty lists, where each sublist will eventually store integers representing the destination stations of candies that start at the corresponding station. Each (a, b) pair read from input satisfies 1 ≤ a, b ≤ n and a ≠ b.
def func_2():
    n, m = map(int, input().split())
    station = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        
        station[a - 1].append(b - 1)
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers such that 2 ≤ `n` ≤ 5000 and 1 ≤ `m` ≤ 20000, `station` is a list of `n` lists where each `station[i]` contains the indices of stations connected to station `i + 1` based on the input pairs `(a, b)`, `i` is `m - 1`, and each `(a, b)` pair read from input satisfies 1 ≤ `a`, `b` ≤ `n` and `a` ≠ `b`. If `m` is 0, the loop does not execute, and `station` remains a list of `n` empty lists.
    max_candy = [0] * n
    for i in range(n):
        try:
            max_candy[i] = min(station[i], key=lambda x: x + n - i if x < i else x - i)
        except ValueError:
            pass
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers such that 2 ≤ `n` ≤ 5000 and 1 ≤ `m` ≤ 20000, `station` is a list of `n` lists where each `station[i]` contains the indices of stations connected to station `i + 1` based on the input pairs `(a, b)`, `i` is `n - 1`, `max_candy` is a list of `n` elements where each element `max_candy[j]` (for 0 ≤ j < n) is the minimum value in `station[j]` based on the custom key function `lambda x: x + n - j if x < j else x - j` if `station[j]` is not empty; otherwise, `max_candy[j]` remains 0.
    for i in range(n):
        res = 0
        
        for j in range(i, i + n):
            if len(station[j % n]) == 0:
                continue
            dist = j - i
            j %= n
            dist += (len(station[j]) - 1) * n + (max_candy[j] + n - j if max_candy[
                j] < j else max_candy[j] - j)
            res = max(res, dist)
        
        print(res, end=' ')
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 5000, `m` is an integer such that 1 ≤ `m` ≤ 20000, `station` is a list of `n` lists where each `station[i]` contains the indices of stations connected to station `i + 1`, `i` is `n`, `max_candy` is a list of `n` elements where each element `max_candy[j]` (for 0 ≤ j < n) is the minimum value in `station[j]` based on the custom key function `lambda x: x + n - j if x < j else x - j` if `station[j]` is not empty; otherwise, `max_candy[j]` remains 0, `res` is the maximum distance calculated over all valid iterations of the loop, or 0 if no valid iterations occur, and `res` is printed `n` times followed by a space.
#Overall this is what the function does:The function `func_2` processes a set of (a, b) pairs, where 1 ≤ a, b ≤ n and a ≠ b, to populate a list `station` of n empty lists. Each sublist `station[i]` stores the indices of stations connected to station `i + 1`. After populating `station`, the function calculates the minimum distance to the closest connected station for each station and stores these values in `max_candy`. Finally, it computes and prints the maximum distance for each starting station, considering all possible paths through the connected stations. The function handles edge cases where no connections exist for a station by skipping those iterations. The function modifies the `station` list in place and prints a sequence of n integers, each representing the maximum distance for the corresponding starting station.

