#State of the program right berfore the function call: meats is a list of tuples, where each tuple contains three integers representing the coordinates (x, y) and hardness (c) of a piece of meat, and K is an integer such that 1 <= K <= len(meats).
def func_1(meats, K, T):
    N = len(meats)
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1, c1 = meats[i]
            x2, y2, c2 = meats[j]
            if c1 * T < c2 * T:
                x1, y1, c1, x2, y2, c2 = x2, y2, c2, x1, y1, c1
            d = c1 * T - c2 * T
            if d < 0:
                continue
            d /= c1 * c2
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2
            dx = (x1 - x2) / 2
            dy = (y1 - y2) / 2
            d2 = dx * dx + dy * dy
            if d * d2 > d2:
                continue
            mx = cx + dy * math.sqrt(d2 * d - d * d) / d2
            my = cy - dx * math.sqrt(d2 * d - d * d) / d2
            count = sum(c * math.sqrt((mx - x) ** 2 + (my - y) ** 2) <= T for x, y,
                c in meats)
            if count >= K:
                return True
        
    #State of the program after the  for loop has been executed: `i` is `N`, `j` is `N - 1`, `dx` is \((x1 - x2) / 2\) where `x1` is the first element of `meats[j]` and `x2` is the first element of `meats[0]` when the loop last executed, `dy` is \((y1 - y2) / 2\) where `y1` is the second element of `meats[j]` and `y2` is the second element of `meats[0]` when the loop last executed, `d2` is \(\left(\frac{x1 - x2}{2}\right)^2 + \left(\frac{y1 - y2}{2}\right)^2\) where `x1` and `y1` are the first and second elements of `meats[j]` respectively, and `x2` and `y2` are the first and second elements of `meats[0]` respectively when the loop last executed, `c1` is the third element of `meats[j]` when the loop last executed, `c2` is the third element of `meats[0]` when the loop last executed, `d` is \(\frac{(c1 \cdot T - c2 \cdot T)}{(c1 \cdot c2)}\) when the loop last executed, `cx` is \((x1 + x2) / 2\) where `x1` and `x2` are the first elements of `meats[j]` and `meats[0]` respectively, `cy` is the average of `y1` and `y2` when the loop last executed, `my` is `cy - dx * math.sqrt(d2 * d - d * d) / d2` when the loop last executed, `count` is the number of tuples in `meats` for which \(c * \mathsqrt{(mx - x)^2 + (my - y)^2} \leq T\) is true when the loop last executed, `N` is the length of `meats`, `T` is a constant, `K` is a constant, and the function returns True if `count >= K` during any iteration of the loop. Otherwise, the function does not return anything and leaves the variables unchanged.
    return False
    #The program returns False
#Overall this is what the function does:The function `func_1` accepts a list of tuples `meats`, where each tuple contains three integers representing the coordinates (x, y) and hardness (c) of a piece of meat, and two integers `K` and `T`. It iterates through all pairs of meat pieces, calculates the midpoint and distance between them, and counts the number of other meat pieces within a distance `T` from this midpoint. If at any point the count of such pieces is greater than or equal to `K`, the function returns `True`. If no such pair of meat pieces satisfy this condition, the function returns `False`.

#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 60, K is an integer such that 1 ≤ K ≤ N, meats is a list of tuples, where each tuple contains three integers representing the coordinates \(x_i, y_i\) and hardness \(c_i\) of the i-th piece of meat, and all coordinates satisfy -1000 ≤ \(x_i, y_i\) ≤ 1000, with no two pieces of meat having the same coordinates.
def func_2(N, K, meats):
    low, high = 0, 1000000000.0
    while high - low > 1e-07:
        mid = (low + high) / 2
        
        if func_1(meats, K, mid):
            high = mid
        else:
            low = mid
        
    #State of the program after the loop has been executed: `N` is an integer such that 1 ≤ N ≤ 60, `K` is an integer such that 1 ≤ K ≤ N, `meats` is a list of tuples where each tuple contains three integers representing the coordinates \(x_i, y_i\) and hardness \(c_i\) of the i-th piece of meat, and all coordinates satisfy -1000 ≤ \(x_i, y_i\) ≤ 1000, with no two pieces of meat having the same coordinates; `low` is 0, `high` is 1000000000.0, `mid` is a value between `low` and `high` such that the difference between `high` and `low` is less than or equal to 1e-07, and `func_1(meats, K, mid)` evaluates to true if `high` is the final value of `high`. If `func_1(meats, K, mid)` evaluates to false, then `low` is the final value of `low`.
    return high
    #`The program returns the value of high which is the final value such that the difference between high and low is less than or equal to 1e-07`
#Overall this is what the function does:The function `func_2` accepts parameters `N`, `K`, and `meats`. It performs a binary search to find the value of `high` such that the difference between `high` and `low` is less than or equal to \(1 \times 10^{-7}\). During the search, it uses the function `func_1` to determine whether a certain condition is met. If `func_1` returns `True`, `high` is updated to `mid`; otherwise, `low` is updated to `mid`. The function ultimately returns the final value of `high` after the loop terminates.

#State of the program right berfore the function call: data is a string containing space-separated integers representing the values of N, K, followed by the coordinates and hardness of N pieces of meat. N and K are positive integers such that 1 <= N <= 60 and 1 <= K <= N. Each piece of meat is represented by three integers (x, y, c) where -1000 <= x, y <= 1000 and 1 <= c <= 100. All (x, y) pairs are unique.
def func_3():
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    meats = []
    index = 2
    for _ in range(N):
        x = int(data[index])
        
        y = int(data[index + 1])
        
        c = int(data[index + 2])
        
        meats.append((x, y, c))
        
        index += 3
        
    #State of the program after the  for loop has been executed: `data` is a list of strings, `N` is the integer value of the first element in `data`, `K` is the integer value of the second element in `data`, `meats` is a list of tuples containing `N` elements, each tuple is `(x, y, c)` where `x`, `y`, and `c` are integers, `index` is `3 * N + 2`, the original values of `x`, `y`, and `c` are the integers corresponding to the elements in `data` starting from `data[2]` and incrementing by 3 for each tuple.
    result = func_2(N, K, meats)
    print(f'{result:.6f}')
#Overall this is what the function does:The function `func_3` accepts a string `data` containing space-separated integers representing the values of `N`, `K`, followed by the coordinates and hardness of `N` pieces of meat. It processes this input to extract the necessary data into variables `N`, `K`, and a list of meat tuples `(x, y, c)`. It then calls `func_2` with `N`, `K`, and the list of meat tuples as arguments. Finally, it prints the result from `func_2` formatted to six decimal places.

