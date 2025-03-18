#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and cas_de_test is a list of tuples, where each tuple contains three integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30, representing the scores of the three players in a non-decreasing order.
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
        
    #State: `t` is an integer such that 1 <= t <= 500, `cas_de_test` is a list of tuples, where each tuple contains three integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30, `resultats` is a list of integers representing the number of draws or -1 for each case in `cas_de_test`.
    return resultats
    #The program returns `resultats`, which is a list of integers representing the number of draws or -1 for each case in `cas_de_test`.
#Overall this is what the function does:The function takes an integer `t` representing the number of test cases and a list `cas_de_test` of tuples, where each tuple contains three integers representing the scores of three players in non-decreasing order. It returns a list of integers, where each integer represents the number of draws for the corresponding test case or -1 if the scores do not satisfy the conditions for a valid match.

