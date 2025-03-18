#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and cas_de_test is a list of lists, where each inner list contains three integers [p_1, p_2, p_3] representing the scores of the three players, sorted non-decreasingly (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30).
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
        
    #State: Output State: The `resultats` list will contain the results of all the valid cases processed by the loop. For each valid case, the value appended to `resultats` will be `egalites // 2`, where `egalites` is calculated as `total_points - 2 * (p3 - p2) - 2 * (p3 - p1)`. If any case does not meet the conditions specified in the loop (i.e., `total_points` is odd, `total_matchs` is greater than 3, or `p3` is greater than `total_matchs`), then `-1` will be appended to `resultats` instead.
    #
    #In summary, `resultats` will be a list of all valid `egalites // 2` values for each set of `[p1, p2, p3]` in `cas_de_test`, with `-1` appended wherever the conditions are not met.
    return resultats
    #The program returns a list `resultats` containing the valid `egalites // 2` values for each set of `[p1, p2, p3]` in `cas_de_test`, with `-1` appended wherever the conditions are not met.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer between 1 and 500, and `cas_de_test`, a list of lists where each inner list contains three integers `[p1, p2, p3]` sorted non-decreasingly. It processes each inner list to calculate the number of equalities (`egalites // 2`) based on specific conditions. If any condition is not met, it appends `-1` to the result list. Finally, it returns a list `resultats` containing the valid `egalites // 2` values for each set of `[p1, p2, p3]` in `cas_de_test`, with `-1` appended wherever the conditions are not met.

