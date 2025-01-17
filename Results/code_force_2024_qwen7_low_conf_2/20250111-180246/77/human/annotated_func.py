#State of the program right berfore the function call: fountain is a tuple containing two positive integers (r, c) representing the row and column coordinates of a fountain on the field, n and m are positive integers representing the dimensions of the field (2 ≤ n, m ≤ 10^9).
def func_1(fountain, n, m):
    r, c = fountain
    diagonal_distance = abs(r + c - (n + 1))
    return max(diagonal_distance // 2, 0)
    #`The program returns max(abs(r + c - (n + 1)) // 2, 0)`
#Overall this is what the function does:The function `func_1` accepts a tuple `fountain` containing the row and column coordinates of a fountain on a field, along with two integers `n` and `m` representing the dimensions of the field. It calculates the value of `max(abs(r + c - (n + 1)) // 2, 0)`, where `r` and `c` are the row and column coordinates from the `fountain` tuple, and returns this value. This calculation effectively computes the maximum distance from the fountain to the "middle" diagonal of the field (which is defined as the line from (1, n) to (m, 1)), adjusted by half a step, ensuring the result is non-negative. Potential edge cases include when the fountain is on the exact middle diagonal, resulting in a distance of 0, and when the coordinates are such that the absolute difference `abs(r + c - (n + 1))` is zero or negative, which the `max` function handles appropriately.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n and m are positive integers such that \(2 \leq n, m \leq 10^9\), and k is a positive integer such that \(2 \leq k \leq 2 \cdot 10^5\). The coordinates of the fountains (r_i, c_i) are pairs of positive integers such that \(1 \leq r_i \leq n\) and \(1 \leq c_i \leq m\), and all fountain coordinates are distinct and none of them is equal to (n, 1).
def func_2():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        m = int(data[index + 1])
        
        k = int(data[index + 2])
        
        index += 3
        
        alpha = (n * m + 1) // 2
        
        additional_areas = []
        
        for __ in range(k):
            r = int(data[index])
            c = int(data[index + 1])
            index += 2
            additional_areas.append(func_1((r, c), n, m))
        
        results.append((alpha, additional_areas))
        
    #State of the program after the  for loop has been executed: `t` is the initial value of `t`, `results` is a list of tuples `(alpha, additional_areas)` where for each tuple: `alpha` is \((n * m + 1) // 2\) with `n` being the integer value of `data[index - 6]` and `m` being the integer value of `data[index - 5]`, and `additional_areas` is a list containing the results of applying `func_1((r, c), n, m)` for each pair `(r, c)` with `r` being the integer value of `data[index - 4 - 2 * j]` and `c` being the integer value of `data[index - 3 - 2 * j]` for `j` in the range of the length of `additional_areas`. `index` is the final value after all iterations of the loop.
    for result in results:
        alpha, additional_areas = result
        
        print(alpha)
        
        print(' '.join(map(str, additional_areas)))
        
    #State of the program after the  for loop has been executed: `results` is a non-empty list; each tuple in `results` is of the form (`alpha`, `additional_areas`); for each tuple in `results`, `alpha` is printed and the elements of `additional_areas` are printed, each on a new line.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads in the dimensions \(n\) and \(m\) of a grid, the number of fountains \(k\), and the coordinates of each fountain. It then calculates a value \(\alpha\) defined as \((n \times m + 1) // 2\). For each fountain, it calls another function `func_1` to compute an additional area related to the fountain's position. The results are stored in a list of tuples, where each tuple contains the value \(\alpha\) and a list of the computed additional areas. Finally, the function prints \(\alpha\) and the computed additional areas for each test case.

