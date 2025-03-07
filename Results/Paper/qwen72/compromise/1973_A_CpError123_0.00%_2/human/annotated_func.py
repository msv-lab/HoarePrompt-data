#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and cas_de_test is a list of tuples, each containing three integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30.
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
        
    #State: Output State: `t` is an integer such that 1 <= t <= 500, `cas_de_test` is a list of tuples, each containing three integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30, `resultats` is a list of integers, each either -1 or the number of ties (egalites) calculated for each tuple in `cas_de_test` based on the loop's conditions.
    return resultats
    #The program returns a list `resultats` of integers, where each integer is either -1 or the number of ties (equalities) calculated for each tuple in `cas_de_test`. Each tuple in `cas_de_test` contains three integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30, and the number of ties is determined based on the conditions specified in the loop.
#Overall this is what the function does:The function `func_1` accepts an integer `t` and a list of tuples `cas_de_test`. Each tuple in `cas_de_test` contains three integers `p_1`, `p_2`, and `p_3` such that 0 <= p_1 <= p_2 <= p_3 <= 30. The function returns a list `resultats` where each element corresponds to a tuple in `cas_de_test`. Each element in `resultats` is either -1 if the conditions for calculating ties are not met, or the number of ties (equalities) calculated based on the conditions specified in the loop. The conditions for calculating ties include: the total points (sum of p_1, p_2, and p_3) being even, the total matches (half of total points) being 3 or less, and p_3 not exceeding the total matches. If these conditions are met, the number of ties is calculated and appended to `resultats`; otherwise, -1 is appended.

