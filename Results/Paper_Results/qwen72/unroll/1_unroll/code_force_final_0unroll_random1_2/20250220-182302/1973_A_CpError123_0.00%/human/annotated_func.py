#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 500, and cas_de_test is a list of tuples, where each tuple contains three integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30.
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
        
    #State: `t` is a positive integer such that 1 <= t <= 500, `cas_de_test` is a list of tuples, where each tuple contains three integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30, `resultats` is a list of integers, where each integer is either -1 or the number of draws calculated based on the conditions in the loop.
    return resultats
    #The program returns the list `resultats` which contains integers, each either -1 or the number of draws calculated based on the conditions in the loop for each tuple in `cas_de_test`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` (1 <= t <= 500) and a list of tuples `cas_de_test`, where each tuple contains three integers `p_1`, `p_2`, and `p_3` (0 <= p_1 <= p_2 <= p_3 <= 30). It processes each tuple to determine the number of draws based on specific conditions and returns a list `resultats` where each element is either -1 (indicating an invalid condition) or the calculated number of draws. The final state of the program includes the original `t` and `cas_de_test` unchanged, and `resultats` containing the results of the draw calculations for each tuple in `cas_de_test`.

