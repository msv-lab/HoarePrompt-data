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
    return resultats
t = 7
cas_de_test = [(0, 0, 0), (0, 1, 1), (0, 2, 3), (3, 3, 3), (3, 4, 5), (1, 1, 10), (0, 0, 6)]
resultats = func_1(t, cas_de_test)
print('\n'.join(map(str, resultats)))