#State of the program right berfore the function call: d is an integer such that 1 ≤ d ≤ 10^5, n and m are integers such that 1 ≤ n, m ≤ 10^5, and each sofa's coordinates (x1, y1) and (x2, y2) are integers satisfying 1 ≤ x1, x2 ≤ n, 1 ≤ y1, y2 ≤ m with (x1, y1) ≠ (x2, y2). Also, cnt_l, cnt_r, cnt_t, and cnt_b are non-negative integers such that 0 ≤ cnt_l, cnt_r, cnt_t, cnt_b ≤ d - 1.
def func():
    d = int(input().strip())
    n, m = map(int, input().strip().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().strip().split())
        
        sofas.append((x1, y1, x2, y2))
        
    #State of the program after the  for loop has been executed: `d` is a user-provided integer such that 1 ≤ `d` ≤ 10^5; `sofas` is a list containing `d` tuples of integers, where each tuple is in the form `(x1, y1, x2, y2)` representing input integers; `cnt_l`, `cnt_r`, `cnt_t`, and `cnt_b` remain unchanged as non-negative integers.
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
        
    #State of the program after the  for loop has been executed: `right_count` is a list where each entry contains the count of sofas where `x1 < x1_j` and `x2 < x1_j` for each sofa, `left_count` is a list where each entry contains the count of sofas where `x1 > x2_j` and `x2 > x2_j`, `bottom_count` is a list where each entry contains the count of sofas where `y1 < y1_j` and `y2 < y1_j`, `top_count` is a list where each entry contains the count of sofas where `y1 > y2_j` and `y2 > y2_j`, `sofas` is a list containing exactly `d` sofa configurations.`
    target_sofa = -1
    for i in range(d):
        if left_count[i] == cnt_l and right_count[i] == cnt_r and top_count[i
            ] == cnt_t and bottom_count[i] == cnt_b:
            target_sofa = i + 1
            break
        
    #State of the program after the  for loop has been executed: `right_count`, `left_count`, `bottom_count`, and `top_count` are lists, `sofas` is a list containing exactly `d` sofa configurations, and `target_sofa` is set to the smallest index (1-based) of a sofa configuration for which `left_count[i]` equals `cnt_l`, `right_count[i]` equals `cnt_r`, `top_count[i]` equals `cnt_t`, and `bottom_count[i]` equals `cnt_b`. If no such index exists, `target_sofa` remains -1. `d` is the total number of configurations.
    print(target_sofa)
#Overall this is what the function does:The function reads input to determine the configuration of multiple sofas based on their coordinates. It accepts user-provided integers for the number of sofa configurations `d`, and two additional integers `n` and `m` that define the space within which sofas are placed. Following this, the function collects the coordinates of `d` sofas in the form of tuples. Then, it retrieves counts (`cnt_l`, `cnt_r`, `cnt_t`, `cnt_b`) which specify how many sofas are located in specific relative positions. The function computes counts for each sofa in relation to all other sofas based on these counts—specifically how many sofas are to the left, right, above, and below each sofa. After calculating these counts, the function checks if any sofa meets the criteria defined by `cnt_l`, `cnt_r`, `cnt_t`, and `cnt_b`. If such a sofa is found, it prints the 1-based index of the first sofa that matches these criteria. If no sofa meets the criteria, it prints -1. The function does not return any values but outputs the index directly. It does not handle invalid inputs explicitly, thus edge cases related to input validation are not addressed in the function.

