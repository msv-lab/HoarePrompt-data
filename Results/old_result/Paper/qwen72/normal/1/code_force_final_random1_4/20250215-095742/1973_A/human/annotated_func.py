#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 ≤ t ≤ 500. Each element in cas_de_test is a tuple of three integers (p_1, p_2, p_3) where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, representing the scores of the three players sorted in non-decreasing order.
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
        
    #State: After all iterations of the loop have completed, `t` remains a positive integer representing the number of test cases, where 1 ≤ t ≤ 500. `cas_de_test` is a list of tuples where each tuple contains three integers (p_1, p_2, p_3) such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30. The length of `cas_de_test` is equal to `t`. `resultats` is a list containing the results of the loop for each tuple in `cas_de_test`. For each tuple (p_1, p_2, p_3) in `cas_de_test`, if the total points (p_1 + p_2 + p_3) is odd, or if the total matches (total points divided by 2) is greater than 3, or if the highest score (p_3) is greater than the total matches, or if the calculated number of ties (total points - 2 * (p_3 - p_2) - 2 * (p_3 - p_1)) is less than 0, then the corresponding entry in `resultats` is -1. Otherwise, the corresponding entry in `resultats` is the number of ties divided by 2.
    return resultats
    #The program returns a list `resultats` where each element corresponds to a tuple in `cas_de_test`. Each element in `resultats` is either -1 or a non-negative integer. If the conditions (total points being odd, total matches > 3, highest score > total matches, or calculated number of ties < 0) are met for a tuple, the corresponding element in `resultats` is -1. Otherwise, the element is the number of ties divided by 2.
#Overall this is what the function does:The function `func_1` takes two parameters: a positive integer `t` representing the number of test cases, and a list `cas_de_test` containing tuples of three integers each, representing the scores of three players in non-decreasing order. It processes each tuple to determine the number of ties (draws) that could have occurred based on the given scores. The function returns a list `resultats` where each element corresponds to a tuple in `cas_de_test`. For each tuple, if the total points are odd, the total matches exceed 3, the highest score is greater than the total matches, or the calculated number of ties is negative, the corresponding element in `resultats` is -1. Otherwise, the element is the number of ties divided by 2.

