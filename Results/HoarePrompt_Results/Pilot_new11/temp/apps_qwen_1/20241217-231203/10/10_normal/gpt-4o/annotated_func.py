#State of the program right berfore the function call: d is an integer such that 1 ≤ d ≤ 10^5, n and m are integers such that 1 ≤ n, m ≤ 10^5, there are d lines each containing four integers x_1, y_1, x_2, y_2 representing the coordinates of the i-th sofa (1 ≤ x_1, x_2 ≤ n, 1 ≤ y_1, y_2 ≤ m, and (x_1, y_1) ≠ (x_2, y_2)), and cnt_l, cnt_r, cnt_t, cnt_b are integers such that 0 ≤ cnt_l, cnt_r, cnt_t, cnt_b ≤ d - 1.
def func():
    d = int(input().strip())
    n, m = map(int, input().strip().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().strip().split())
        
        sofas.append((x1, y1, x2, y2))
        
    #State of the program after the  for loop has been executed: `sofas` is a list of tuples, each tuple containing four integers (x1, y1, x2, y2) representing the coordinates of sofas; `d` is a positive integer within its specified range.
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().strip().split())
    left_count = [0] * d
    right_count = [0] * d
    top_count = [0] * d
    bottom_count = [0] * d
    for i in range(d):
        x1, y1, x2, y2 = sofas[i]
        
        for j in range(d):
            if i == j:
                continue
            x1_j, y1_j, x2_j, y2_j = sofas[j]
            if x1 < x1_j and x2 < x1_j:
                right_count[i] += 1
            if x1 > x2_j and x2 > x2_j:
                left_count[i] += 1
            if y1 < y1_j and y2 < y1_j:
                bottom_count[i] += 1
            if y1 > y2_j and y2 > y2_j:
                top_count[i] += 1
        
    #State of the program after the  for loop has been executed: `sofas` is a non-empty list of tuples, each tuple containing four integers (x1, y1, x2, y2) representing the coordinates of sofas; `d` is a positive integer; `left_count[i]` is the count of sofas that satisfy `x1 > x2_j` and `x2 > x2_j` for each `j` in the range `0` to `d-1` for each `i` in the range `0` to `d-1`; `right_count[i]` is the count of sofas that satisfy `x1 < x1_j` and `x2 < x1_j` for each `j` in the range `0` to `d-1` for each `i` in the range `0` to `d-1`; `top_count[i]` is the count of sofas that satisfy `y1 > y2_j` and `y2 > y2_j` for each `j` in the range `0` to `d-1` for each `i` in the range `0` to `d-1`; `bottom_count[i]` is the count of sofas that satisfy `y1 < y1_j` and `y2 < y1_j` for each `j` in the range `0` to `d-1` for each `i` in the range `0` to `d-1`.
    target_sofa = -1
    for i in range(d):
        if left_count[i] == cnt_l and right_count[i] == cnt_r and top_count[i
            ] == cnt_t and bottom_count[i] == cnt_b:
            target_sofa = i + 1
            break
        
    #State of the program after the  for loop has been executed: `sofas` is a non-empty list of tuples, each tuple containing four integers (x1, y1, x2, y2) representing the coordinates of sofas, `d` is a positive integer, `target_sofa` is either `-1` or an integer in the range `1` to `d`, depending on whether any index `i` satisfies the condition `left_count[i] == cnt_l and right_count[i] == cnt_r and top_count[i] == cnt_t and bottom_count[i] == cnt_b`. If no such `i` exists, `target_sofa` remains `-1`.
    print(target_sofa)
#Overall this is what the function does:The function processes a set of sofas' coordinates provided by the user and determines if there exists a sofa whose number of left, right, top, and bottom neighbors matches the given counts `cnt_l`, `cnt_r`, `cnt_t`, and `cnt_b`. If such a sofa is found, it prints the sofa's index (1-based); otherwise, it prints `-1`. The function reads the following inputs: the number of sofas `d`, the dimensions of the grid `n` and `m`, the coordinates of each sofa, and the counts of left, right, top, and bottom neighbors. The function does not return any value explicitly, but its output is printed to the console.

