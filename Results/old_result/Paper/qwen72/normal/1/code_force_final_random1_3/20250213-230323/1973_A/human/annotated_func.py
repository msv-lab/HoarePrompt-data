#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 ≤ t ≤ 500. cas_de_test is a list of tuples, each containing three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order.
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
        
    #State: After the loop has executed all iterations, `t` remains a positive integer representing the number of test cases, where 1 ≤ t ≤ 500. The list `cas_de_test` remains unchanged and contains `t` tuples, each with three integers `p_1`, `p_2`, and `p_3` (0 ≤ `p_1` ≤ `p_2` ≤ `p_3` ≤ 30). The list `resultats` will contain `t` elements, where each element corresponds to the result of processing one tuple from `cas_de_test`. For each tuple `(p1, p2, p3)`, if the total points (`p1 + p2 + p3`) are odd, or if the total matches (`total_points // 2`) is greater than 3, or if `p3` is greater than the total matches, or if the number of ties (`egalites`) is negative, then `-1` is appended to `resultats`. Otherwise, the number of ties (`egalites // 2`) is appended to `resultats`.
    return resultats
    #The program returns a list `resultats` containing `t` elements, where each element is either the number of ties (`egalites // 2`) or `-1` based on the conditions specified for each tuple `(p1, p2, p3)` in the list `cas_de_test`. Each tuple's result is determined by checking if the total points (`p1 + p2 + p3`) are odd, if the total matches (`total_points // 2`) is greater than 3, if `p3` is greater than the total matches, or if the number of ties (`egalites`) is negative. If any of these conditions are true, `-1` is appended; otherwise, the number of ties (`egalites // 2`) is appended.
#Overall this is what the function does:The function `func_1` takes two parameters: a positive integer `t` (1 ≤ t ≤ 500) representing the number of test cases, and a list `cas_de_test` containing `t` tuples, each with three integers (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of three players in a game. The function processes each tuple to determine the number of ties or if the game is invalid. It returns a list `resultats` of length `t`, where each element is either the number of ties divided by 2 or -1. Specifically, for each tuple `(p1, p2, p3)`, if the total points (`p1 + p2 + p3`) are odd, or if the total matches (`total_points // 2`) is greater than 3, or if `p3` is greater than the total matches, or if the number of ties (`egalites`) is negative, then `-1` is appended to `resultats`. Otherwise, the number of ties (`egalites // 2`) is appended. The original list `cas_de_test` remains unchanged.

