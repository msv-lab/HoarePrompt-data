#State of the program right berfore the function call: the input follows the given format: the first line contains an integer d (1 ≤ d ≤ 10^5) representing the number of sofas, the second line contains two integers n and m (1 ≤ n, m ≤ 10^5) representing the size of the storehouse, the next d lines contain four integers x_1, y_1, x_2, y_2 representing the coordinates of each sofa, and the last line contains four integers cnt_{l}, cnt_{r}, cnt_{t}, cnt_{b} (0 ≤ cnt_{l}, cnt_{r}, cnt_{t}, cnt_{b} ≤ d - 1) representing the number of sofas to the left, right, top, and bottom of Grandpa Maks's sofa, respectively.
def func():
    d = int(input().strip())
    n, m = map(int, input().strip().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().strip().split())
        
        sofas.append((x1, y1, x2, y2))
        
    #State of the program after the  for loop has been executed: `d` is a non-negative integer, `n` is the number of rows of the storehouse, `m` is the number of columns of the storehouse, `sofas` is a list containing `d` tuples of sofa coordinates, where each tuple contains four integers representing the coordinates of a sofa
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
        
    #State of the program after the  for loop has been executed: `d` is a non-negative integer, `n` is the number of rows of the storehouse, `m` is the number of columns of the storehouse, `sofas` is a list containing `d` tuples of sofa coordinates, `cnt_l`, `cnt_r`, `cnt_t`, `cnt_b` are input integers, `left_count` is a list of length `d` where each value at index `i` represents the number of sofas to the left of the sofa at index `i`, `right_count` is a list of length `d` where each value at index `i` represents the number of sofas to the right of the sofa at index `i`, `top_count` is a list of length `d` where each value at index `i` represents the number of sofas below the sofa at index `i`, `bottom_count` is a list of length `d` where each value at index `i` represents the number of sofas above the sofa at index `i`, with all counts being updated based on the relative positions of the sofas in the `sofas` list, or all counts are lists of zeros if `d` is 0.
    target_sofa = -1
    for i in range(d):
        if left_count[i] == cnt_l and right_count[i] == cnt_r and top_count[i
            ] == cnt_t and bottom_count[i] == cnt_b:
            target_sofa = i + 1
            break
        
    #State of the program after the  for loop has been executed: `d` is a non-negative integer, `n` is the number of rows of the storehouse, `m` is the number of columns of the storehouse, `sofas` is a list containing `d` tuples of sofa coordinates, `cnt_l`, `cnt_r`, `cnt_t`, `cnt_b` are input integers, `left_count` is a list of length `d` where each value at index `i` represents the number of sofas to the left of the sofa at index `i`, `right_count` is a list of length `d` where each value at index `i` represents the number of sofas to the right of the sofa at index `i`, `top_count` is a list of length `d` where each value at index `i` represents the number of sofas below the sofa at index `i`, `bottom_count` is a list of length `d` where each value at index `i` represents the number of sofas above the sofa at index `i`, `target_sofa` is either -1 if no sofa matches the given counts or the index plus one of the first sofa that matches the given counts, and `i` is `d-1` if the loop completes all iterations without finding a match.
    print(target_sofa)
#Overall this is what the function does:The function processes input related to the number of sofas, storehouse size, sofa coordinates, and sofa positions relative to Grandpa Maks's sofa, calculates the number of sofas to the left, right, top, and bottom of each sofa, and prints the index plus one of the first sofa that matches the given counts, or -1 if no matching sofa is found, while assuming valid input and not handling potential exceptions or edge cases.

