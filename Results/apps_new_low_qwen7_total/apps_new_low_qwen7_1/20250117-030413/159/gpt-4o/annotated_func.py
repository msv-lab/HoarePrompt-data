#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the second line contains 2·n integers a_1, a_2, ... a_{2n} such that 1 ≤ a_{i} ≤ 1000.
def func():
    n = int(input())

ratings = list(map(int, input().split()))

ratings.sort()

team1 = ratings[:n]

team2 = ratings[n:]

possible = all(team1[i] < team2[i] for i in range(n))
    if possible :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer, `k` is an integer, `ratings` is a list of 2k integers sorted in ascending order, `team1` is the first k elements of `ratings`, `team2` is the last k elements of `ratings`. If `possible` is True, the function prints 'YES'. Otherwise, if `possible` is False, the function prints 'NO'.
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and 2·n integers (1 ≤ a_{i} ≤ 1000) as input. It then sorts these integers into two teams (`team1` and `team2`) of size `n` each. The function checks whether every element in `team1` is strictly less than the corresponding element in `team2`. If this condition holds for all elements, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. Potential edge cases include when `n` is at the boundary values (1 or 100), and the input values are at their boundary conditions (1 or 1000). The function does not handle cases where the input does not meet the specified constraints (e.g., `n` outside the range [1, 100] or `a_i` outside the range [1, 1000]).

