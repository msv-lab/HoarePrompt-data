#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and cas_de_test is a list of tuples where each tuple contains three integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30. Each tuple represents the scores of the three players for a single test case.
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
        
    #State: resultats is a list of integers calculated based on the conditions described, t is unchanged, and cas_de_test is unchanged.
    return resultats
    #The program returns the list 'resultats' which contains integers calculated based on the conditions described.
#Overall this is what the function does:The function processes a list of test cases, each consisting of scores for three players. It calculates and returns a list of integers where each integer represents the number of matches that ended in a draw for the corresponding test case, or -1 if the scores do not meet the specified conditions.

