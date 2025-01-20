#State of the program right berfore the function call: The input is a list of tuples, where each tuple contains two integers representing the x and y coordinates of a vector starting from the origin. The length of the list is an integer n such that 2 ≤ n ≤ 100 000, and each coordinate (x_i, y_i) satisfies |x_i|, |y_i| ≤ 10 000 and x_i^2 + y_i^2 > 0. No two vectors have the same direction, but they can have opposite directions.
def func():
    n = int(input())

v = []
    for _ in range(n):
        x, y = map(int, input().split())
        
        v.append((x, y))
        
    #State of the program after the  for loop has been executed: n is greater than or equal to 0, x is any integer, y is any integer, v is a list containing tuples (X1, Y1), (X2, Y2), ..., (Xn, Yn) where (Xi, Yi) are integers entered in each iteration of the loop.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` equals `min(n, 100)`, `j` equals `min(n, i + 99)`, `ans_angle` is the minimum value of all angles calculated during the loop, and `ans` is a tuple containing the indices of the two vectors that yield the smallest angle among all pairs `(v[i], v[j])` where `i < j <= min(n, i + 100)` and `i` ranges up to `min(n, 100)`.
    print(ans[0] + 1, ans[1] + 1)
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains two integers representing the x and y coordinates of a vector starting from the origin. It sorts these vectors in counterclockwise order around the origin. Then, it finds the pair of vectors with the smallest angle between them, considering only the first 100 vectors or all vectors if there are fewer than 100. Finally, it prints the 1-based indices of these two vectors.

