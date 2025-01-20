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
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ n ≤ 100, `ratings` is a sorted list of 2·n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_{i} ≤ 1000, `team1` is the first n elements of the sorted `ratings` list, `team2` is the last n elements of the sorted `ratings` list, `possible` is a boolean indicating whether each element in `team1` is less than or equal to the corresponding element in `team2`. If `possible` is true, then `possible` remains true. If `possible` is false, the console prints 'NO'.
#Overall this is what the function does:The function `func()` accepts an integer `n` such that \(1 \leq n \leq 100\) and \(2 \cdot n\) integers \(a_1, a_2, \ldots, a_{2n}\) such that \(1 \leq a_i \leq 1000\). It sorts these integers into two teams (`team1` and `team2`) of size `n` each. The function then checks if every element in `team1` is strictly less than the corresponding element in `team2`. If this condition holds for all pairs, the function prints 'YES'. Otherwise, it prints 'NO'. The function does not return any value; instead, it outputs either 'YES' or 'NO' based on the comparison of the two teams. Potential edge cases include when `n` is at the boundaries of its range (i.e., `n=1` or `n=100`). Additionally, if the input integers do not satisfy the constraints \(1 \leq a_i \leq 1000\), the function will still proceed with the sorting and comparison, which might lead to unexpected results if the annotations are not updated to reflect this behavior.

