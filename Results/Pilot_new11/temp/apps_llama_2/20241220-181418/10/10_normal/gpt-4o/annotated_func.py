#State of the program right berfore the function call: The input includes several parameters: the number of sofas (d) which is an integer greater than or equal to 1 and less than or equal to 10^5, the size of the storehouse (n, m) which are integers greater than or equal to 1 and less than or equal to 10^5, the coordinates of the sofas (x1, y1, x2, y2) which are integers greater than or equal to 1 and less than or equal to n and m respectively, and the number of sofas to the left, right, top, and bottom (cntl, cntr, cntt, cntb) which are integers greater than or equal to 0 and less than or equal to d - 1. All sofas are distinct, no cell is covered by more than one sofa, and cells (x1, y1) and (x2, y2) have a common side and are not equal.
def func():
    d = int(input().strip())
    n, m = map(int, input().strip().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().strip().split())
        
        sofas.append((x1, y1, x2, y2))
        
    #State of the program after the  for loop has been executed: `d` is an integer between 1 and 10^5, `n` is an input integer, `m` is an input integer, `x1`, `y1`, `x2`, `y2` are the latest input integers between 1 and `n` and between 1 and `m` respectively, `cntl`, `cntr`, `cntt`, `cntb` are integers greater than or equal to 0 and less than or equal to `d - 1`, and `sofas` is a list containing `d` tuple elements, each representing the input coordinates from each iteration.
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
        
    #State of the program after the  for loop has been executed: `d` is an integer between 1 and 10^5, `n` is an input integer, `m` is an input integer, `x1`, `y1`, `x2`, `y2` are the coordinates of the last sofa, `cntl`, `cntr`, `cntt`, `cntb` are input integers, `sofas` is a list of `d` tuple elements representing all input coordinates, `left_count` is a list where each element is the number of sofas to the right of the corresponding sofa, `right_count` is a list where each element is the number of sofas to the left of the corresponding sofa, `top_count` is a list where each element is the number of sofas below the corresponding sofa, `bottom_count` is a list where each element is the number of sofas above the corresponding sofa.
    target_sofa = -1
    for i in range(d):
        if left_count[i] == cnt_l and right_count[i] == cnt_r and top_count[i
            ] == cnt_t and bottom_count[i] == cnt_b:
            target_sofa = i + 1
            break
        
    #State of the program after the  for loop has been executed: `d` is an integer between 1 and 10^5, `n`, `m`, `x1`, `y1`, `x2`, `y2`, `cntl`, `cntr`, `cntt`, `cntb` are input integers, `sofas` is a list of `d` tuple elements, `left_count`, `right_count`, `top_count`, `bottom_count` are lists of counts, and `target_sofa` is either -1 if no sofa matches the input counts or the position (1-indexed) of the first sofa that matches the input counts `cntl`, `cntr`, `cntt`, `cntb`.
    print(target_sofa)
#Overall this is what the function does:The function determines the position of a target sofa in a storehouse based on the provided sofa coordinates and the number of sofas in different directions. It accepts parameters related to the number of sofas, storehouse size, sofa coordinates, and the number of sofas to the left, right, top, and bottom. The function iterates through the list of sofas, calculates the number of sofas in each direction for each sofa, and checks if these counts match the input counts. If a match is found, it returns the 1-indexed position of the target sofa. If no match is found, it returns -1. The function handles cases where there are multiple sofas with the same counts, but it only returns the position of the first matching sofa. It also handles edge cases where the input counts are not found among any of the sofas, returning -1 in such cases. The function assumes that the input is valid and does not perform any error checking on the input values.

