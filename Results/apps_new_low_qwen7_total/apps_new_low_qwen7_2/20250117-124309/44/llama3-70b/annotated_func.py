#State of the program right berfore the function call: The input consists of two parts: first, an integer n representing the number of vectors (2 ≤ n ≤ 100 000), and second, n lines, each containing two integers x_i and y_i representing the coordinates of the i-th vector (|x_i|, |y_i| ≤ 10 000, x_i^2 + y_i^2 > 0). No two vectors share the same direction but can have opposite directions.
def func():
    n = int(input())

v = []
    for _ in range(n):
        x, y = map(int, input().split())
        
        v.append((x, y))
        
    #State of the program after the  for loop has been executed: n is an integer and greater than 0, v is a list of length 2n, x is the last input_x received, y is the last input_y received.
    ans = 0, 1

ans_angle = math.pi

v.sort(key=lambda v: math.atan2(v[1], v[0]))
    for i in range(n):
        for j in range(i + 1, min(n, i + 100)):
            angle = math.acos((v[i][0] * v[j][0] + v[i][1] * v[j][1]) / math.sqrt(v
                [i][0] ** 2 + v[i][1] ** 2) / math.sqrt(v[j][0] ** 2 + v[j][1] ** 2))
            if angle < ans_angle:
                ans_angle = angle
                ans = i, j
        
    #State of the program after the  for loop has been executed: `i` is `n-1`, `j` is the index of `v` that gives the smallest angle with `v[n-1]` when `i` is `n-1`, `ans` is `(n-1, j)`, and `ans_angle` is the minimum angle found between `v[n-1]` and any other vector `v[j]` in the list.
    print(ans[0] + 1, ans[1] + 1)
#Overall this is what the function does:The function reads an integer \( n \) and then \( n \) pairs of integers \((x_i, y_i)\) from the standard input, representing vectors. It sorts these vectors based on their polar angles and then finds the pair of vectors with the smallest angle between them. The function outputs the indices (1-based) of these two vectors. If the number of vectors \( n \) exceeds 100, the function only considers the first 100 vectors for finding the smallest angle.

