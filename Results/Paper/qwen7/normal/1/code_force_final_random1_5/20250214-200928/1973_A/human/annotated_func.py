#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and cas_de_test is a list of lists, where each inner list contains three non-negative integers p_1, p_2, and p_3 such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
def func_1(t, cas_de_test):
    resultats = []
    for (p1, p2, p3) in cas_de_test:
        total_points = p1 + p2 + p3
        
        if total_points % 2 != 0:
            resultats.append(-1)
            continue
        
        total_matchs = total_points // 2
        
        if total_matchs > 3 or p3 > total_matchs:
            resultats.append(-1)
            continue
        
        egalites = total_points - 2 * (p3 - p2) - 2 * (p3 - p1)
        
        if egalites < 0:
            resultats.append(-1)
        else:
            resultats.append(egalites // 2)
        
    #State: Output State: The `resultats` list will contain the final results for all the tuples in `cas_de_test`. For each tuple `(p1, p2, p3)` in `cas_de_test`, the loop will compute `total_points = p1 + p2 + p3`, `total_matchs = total_points // 2`, and `egalites = total_points - 2 * (p3 - p2) - 2 * (p3 - p1)`. Depending on the conditions, `resultats` will append either `-1` or `egalites // 2` to itself. After all iterations, `resultats` will be a list containing the results for each tuple in `cas_de_test`, with `-1` appended if any condition fails, otherwise `egalites // 2`.
    #
    #The `total_matchs` and `egalites` variables will be recalculated for each tuple, but their specific values are not preserved outside the loop as they are used only within the loop body. The `total_points` variable will also be recalculated for each tuple but similarly does not persist outside the loop.
    return resultats
    #The program returns a list named `resultats` which contains the results for each tuple in `cas_de_test`. For each tuple `(p1, p2, p3)`, the program calculates `total_points = p1 + p2 + p3`, `total_matchs = total_points // 2`, and `egalites = total_points - 2 * (p3 - p2) - 2 * (p3 - p1)`. Depending on certain conditions, the list `resultats` appends either `-1` or `egalites // 2` to itself. If any condition fails during the iteration, `-1` is appended; otherwise, `egalites // 2` is appended.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer between 1 and 500, and `cas_de_test`, a list of lists where each inner list contains three non-negative integers `p1`, `p2`, and `p3` such that `0 ≤ p1 ≤ p2 ≤ p3 ≤ 30`. It returns a list named `resultats` containing the results for each tuple in `cas_de_test`. For each tuple `(p1, p2, p3)`, it calculates `total_points = p1 + p2 + p3`, `total_matchs = total_points // 2`, and `egalites = total_points - 2 * (p3 - p2) - 2 * (p3 - p1)`. If certain conditions are met, it appends `egalites // 2` to `resultats`; otherwise, it appends `-1`.

