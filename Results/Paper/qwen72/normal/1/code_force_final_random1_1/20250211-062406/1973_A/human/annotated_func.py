#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 500), representing the number of test cases. cas_de_test is a list of tuples, where each tuple contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30), representing the scores of the three players in each test case.
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
        
    #State: After all iterations of the loop, `t` is a positive integer (1 ≤ t ≤ 500), `cas_de_test` is a list of tuples with `t` tuples, and `resultats` is a list containing `t` elements. Each element in `resultats` corresponds to the result of the respective tuple in `cas_de_test`. For each tuple `(p1, p2, p3)` in `cas_de_test`:
    #- If the sum of `p1`, `p2`, and `p3` (`total_points`) is odd, the corresponding element in `resultats` is `-1`.
    #- If `total_points` is even, `total_matchs` is calculated as `total_points // 2`. If `total_matchs` is greater than 3 or `p3` is greater than `total_matchs`, the corresponding element in `resultats` is `-1`.
    #- If neither of the above conditions is met, `egalites` is calculated as `total_points - 2 * (p3 - p2) - 2 * (p3 - p1)`. If `egalites` is less than 0, the corresponding element in `resultats` is `-1`. Otherwise, the corresponding element in `resultats` is `egalites // 2`.
    return resultats
    #The program returns a list `resultats` containing `t` elements, where each element corresponds to the result of the respective tuple in `cas_de_test`. Each element in `resultats` is calculated based on the conditions specified: if the sum of the tuple elements is odd, the result is `-1`; if the sum is even, further checks are made to determine if the result should be `-1` or the calculated value of `egalites` divided by 2.
#Overall this is what the function does:The function `func_1` takes two parameters: a positive integer `t` (1 ≤ t ≤ 500) representing the number of test cases, and a list `cas_de_test` of `t` tuples, where each tuple contains three integers (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of three players. The function returns a list `resultats` of length `t`, where each element corresponds to the result of the respective tuple in `cas_de_test`. For each tuple `(p1, p2, p3)` in `cas_de_test`:
- If the sum of the scores (`p1 + p2 + p3`) is odd, the corresponding element in `resultats` is `-1`.
- If the sum is even, the function calculates `total_matchs` as half of the sum. If `total_matchs` is greater than 3 or `p3` is greater than `total_matchs`, the corresponding element in `resultats` is `-1`.
- If neither of the above conditions is met, the function calculates `egalites` as `total_points - 2 * (p3 - p2) - 2 * (p3 - p1)`. If `egalites` is less than 0, the corresponding element in `resultats` is `-1`. Otherwise, the corresponding element in `resultats` is `egalites // 2`.

