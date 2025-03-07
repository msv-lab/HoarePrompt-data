#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and cas_de_test is a list of lists where each inner list contains three non-negative integers p_1, p_2, and p_3 such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 500, `cas_de_test` is a list of lists where each inner list contains three non-negative integers p_1, p_2, and p_3 such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30; `resultats` is a list of integers where each element is either -1 or the result of `egalites // 2` after passing all conditions in the loop.
    return resultats
    #The program returns a list of integers called 'resultats', where each element is either -1 or the result of 'egalites // 2' after passing all conditions in the loop.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer between 1 and 500, and `cas_de_test`, a list of lists where each inner list contains three non-negative integers \( p_1 \), \( p_2 \), and \( p_3 \) such that \( 0 \leq p_1 \leq p_2 \leq p_3 \leq 30 \). It processes each inner list in `cas_de_test` to calculate a value `egalites // 2` under certain conditions. If any condition fails, it appends `-1` to the result list. Finally, it returns a list of integers, where each element is either `-1` or the calculated value `egalites // 2`.

