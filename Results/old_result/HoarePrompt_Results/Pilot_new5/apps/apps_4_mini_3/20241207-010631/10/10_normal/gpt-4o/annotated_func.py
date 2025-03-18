#State of the program right berfore the function call: d is a positive integer (1 ≤ d ≤ 10^5) representing the number of sofas; n and m are positive integers (1 ≤ n, m ≤ 10^5) representing the dimensions of the storehouse; each of the next d lines contains four integers (x_1, y_1, x_2, y_2) representing the coordinates of each sofa such that (1 ≤ x_1, x_2 ≤ n, 1 ≤ y_1, y_2 ≤ m), and the last line contains four integers (cnt_l, cnt_r, cnt_t, cnt_b) representing the counts of sofas around Grandpa Maks's sofa (0 ≤ cnt_l, cnt_r, cnt_t, cnt_b ≤ d - 1).
def func():
    d = int(input().strip())
    n, m = map(int, input().strip().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().strip().split())
        
        sofas.append((x1, y1, x2, y2))
        
    #State of the program after the  for loop has been executed: `d` is a non-negative integer, `n` is an input positive integer, `m` is an input positive integer, `sofas` is a list containing `d` tuples of the form (x1, y1, x2, y2), where each tuple corresponds to the input integers provided during each iteration of the loop.
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
        
    #State of the program after the  for loop has been executed: `right_count[i]` is equal to the count of sofas to the right of `sofas[i]`, `left_count[i]` is equal to the count of sofas to the left of `sofas[i]`, `bottom_count[i]` is equal to the count of sofas below `sofas[i]`, `top_count[i]` is equal to the count of sofas above `sofas[i]`, `i` is `d`, `j` is `d`, and `sofas` is a list of at least `d` sofas. If `d` is 0, the counts will remain at their initial values of 0.
    target_sofa = -1
    for i in range(d):
        if left_count[i] == cnt_l and right_count[i] == cnt_r and top_count[i
            ] == cnt_t and bottom_count[i] == cnt_b:
            target_sofa = i + 1
            break
        
    #State of the program after the  for loop has been executed: `right_count[i]`, `left_count[i]`, `bottom_count[i]`, `top_count[i]` represent the counts of sofas as defined, and `target_sofa` is set to the index of the first sofa (1-based) that meets the conditions `left_count[i] == cnt_l`, `right_count[i] == cnt_r`, `top_count[i] == cnt_t`, and `bottom_count[i] == cnt_b`, or remains -1 if no such sofa is found. `i` is equal to `d` after all iterations.
    print(target_sofa)
#Overall this is what the function does:The function reads the number of sofas and the dimensions of a storehouse, then collects the coordinates of each sofa into a list. It counts how many sofas are located to the left, right, above, and below each sofa. Finally, it searches for the first sofa that matches specific criteria regarding the counts of neighboring sofas and prints its 1-based index. If no such sofa is found, it prints -1. The function does not accept parameters directly but relies on user input for its execution.

