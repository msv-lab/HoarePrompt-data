#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and cas_de_test is a list of lists, where each inner list contains three non-negative integers p_1, p_2, and p_3 such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
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
        
    #State: Output State: The `resultats` list will contain one of the following based on the conditions checked within the loop for each inner list in `cas_de_test`:
    #
    #- If any of the conditions cause `-1` to be appended to `resultats`, then `resultats` will end up being a list of `-1`s, with the length equal to the number of inner lists in `cas_de_test`.
    #- If none of the conditions cause `-1` to be appended and all `egalites // 2` values are valid, then `resultats` will be a list containing these valid `egalites // 2` values.
    #
    #The `p1`, `p2`, and `p3` variables will be the last values from the last inner list processed in `cas_de_test`. The `total_points` will be the sum of the last `p1`, `p2`, and `p3`. `total_matchs` will be `total_points // 2`. `egalites` will be calculated as `total_points - 2 * (p3 - p2) - 2 * (p3 - p1)`, and if it's non-negative, `egalites // 2` will be appended to `resultats`.
    #
    #If all inner lists in `cas_de_test` pass all conditions without appending `-1`, the final `resultats` will be a list of `egalites // 2` values for each inner list. If any inner list causes `-1` to be appended, `resultats` will consist of `-1`s followed by any valid `egalites // 2` values.
    return resultats
    #The program returns a list `resultats` which contains either `-1` for each inner list in `cas_de_test` if any condition causes `-1` to be appended, or `egalites // 2` for each valid inner list in `cas_de_test` if no `-1` is appended. The variables `p1`, `p2`, and `p3` are the last values from the last inner list processed in `cas_de_test`. `total_points` is the sum of the last `p1`, `p2`, and `p3`. `total_matchs` is `total_points // 2`. `egalites` is calculated as `total_points - 2 * (p3 - p2) - 2 * (p3 - p1)`, and if it's non-negative, `egalites // 2` is appended to `resultats`.
#Overall this is what the function does:The function `func_1` takes two parameters: `t`, a positive integer between 1 and 500, and `cas_de_test`, a list of lists where each inner list contains three non-negative integers `p1`, `p2`, and `p3` such that `0 ≤ p1 ≤ p2 ≤ p3 ≤ 30`. For each inner list in `cas_de_test`, it checks several conditions. If any condition fails, `-1` is appended to the result list `resultats`. If all conditions pass, `egalites // 2` is appended to `resultats`. After processing all inner lists, the function returns the list `resultats`. The variables `p1`, `p2`, and `p3` hold the last values from the last inner list processed, `total_points` is the sum of the last `p1`, `p2`, and `p3`, `total_matchs` is `total_points // 2`, and `egalites` is calculated as `total_points - 2 * (p3 - p2) - 2 * (p3 - p1)`, with `egalites // 2` appended to `resultats` if non-negative.

