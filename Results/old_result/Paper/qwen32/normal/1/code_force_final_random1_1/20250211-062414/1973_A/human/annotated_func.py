#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and cas_de_test is a list of tuples where each tuple contains three integers (p_1, p_2, p_3) such that 0 <= p_1 <= p_2 <= p_3 <= 30, representing the scores of the three players in non-decreasing order for each test case.
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
        
    #State: `t` is an integer such that 1 <= t <= 500, `cas_de_test` is a list of tuples where each tuple contains three integers (p_1, p_2, p_3) such that 0 <= p_1 <= p_2 <= p_3 <= 30, and `resultats` is a list containing the results of each iteration based on the conditions specified in the loop.
    return resultats
    #The program returns the list `resultats` which contains the results of each iteration based on the conditions specified in the loop.
#Overall this is what the function does:The function takes an integer `t` representing the number of test cases and a list `cas_de_test` of tuples, where each tuple contains three integers representing the scores of three players in non-decreasing order. It returns a list `resultats` where each element corresponds to the result of a test case based on specific conditions related to the total points and individual player scores. If the conditions are not met, the result for that test case is `-1`.

