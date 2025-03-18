#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and cas_de_test is a list of tuples, each containing three integers p_1, p_2, and p_3 where 0 <= p_1 <= p_2 <= p_3 <= 30.
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
        
    #State: Output State: `t` is an integer such that 1 <= t <= 500, `cas_de_test` is a list of tuples, each containing three integers p_1, p_2, and p_3 where 0 <= p_1 <= p_2 <= p_3 <= 30, `resultats` is a list of integers, each representing the number of draws (egalites) for the corresponding tuple in `cas_de_test` or -1 if the conditions for calculating draws are not met.
    return resultats
    #The program returns the list `resultats`, where each element is an integer representing the number of draws (egalites) for the corresponding tuple in `cas_de_test`, or -1 if the conditions for calculating draws are not met.
#Overall this is what the function does:The function `func_1` accepts an integer `t` and a list of tuples `cas_de_test`, where each tuple contains three integers. It processes each tuple to calculate the number of draws (egalites) based on the total points and certain conditions. The function returns a list `resultats` where each element is either the number of draws for the corresponding tuple in `cas_de_test` or -1 if the conditions for calculating draws are not met. The input parameters `t` and `cas_de_test` remain unchanged after the function call.

