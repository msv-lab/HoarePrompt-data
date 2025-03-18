#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and cas_de_test is a list of lists where each inner list contains three non-negative integers p_1, p_2, and p_3 representing the scores of the three players in each test case, sorted non-decreasingly such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
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
        
    #State: Output State: `t` is a positive integer representing the number of test cases, `cas_de_test` is a list of lists where each inner list contains three non-negative integers p_1, p_2, and p_3 representing the scores of the three players in each test case, sorted non-decreasingly such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30; `resultats` is a list containing the number of draws for each valid test case, and -1 for invalid cases.
    return resultats
    #`The program returns a list of results where each element is the number of draws for each valid test case, and -1 for invalid cases`.
#Overall this is what the function does:The function accepts two parameters: `t`, a positive integer representing the number of test cases, and `cas_de_test`, a list of lists where each inner list contains three non-negative integers representing the scores of three players, sorted non-decreasingly. It processes each test case to determine the number of draws between the players based on their scores. If the total points are odd or exceed the maximum allowed points, or if the highest score exceeds half the total points, it records `-1` for that test case indicating an invalid scenario. Otherwise, it calculates and records the number of draws. Finally, it returns a list of results where each element is the number of draws for each valid test case, and `-1` for invalid cases.

