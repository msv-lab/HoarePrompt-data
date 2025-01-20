#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the second line contains 2·n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_{i} ≤ 1000.
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
    #State of the program after the if-else block has been executed: `n` is an integer, `ratings` is a sorted list of 2*n integers, `team1` is a list of the first n elements of `ratings`, `team2` is a list of the last n elements of `ratings`, `possible` is a boolean value indicating if each element in `team1` is less than the corresponding element in `team2`. If `possible` is true, the function prints 'YES'. Otherwise, it does not print anything.
#Overall this is what the function does:The function accepts an integer `n` such that \(1 \leq n \leq 100\) and a list of \(2n\) integers \(a_1, a_2, \ldots, a_{2n}\) where \(1 \leq a_i \leq 1000\). It then sorts these integers and divides them into two teams (`team1` and `team2`). The function checks if every member of `team1` is strictly less than the corresponding member in `team2`. If this condition is met, the function prints 'YES'. Otherwise, it prints 'NO' if such a configuration is not possible. The function handles the case where the input constraints are satisfied, but does not explicitly handle cases where `n` is out of the specified range (though it would raise an error in practice due to invalid input handling outside the function scope).

