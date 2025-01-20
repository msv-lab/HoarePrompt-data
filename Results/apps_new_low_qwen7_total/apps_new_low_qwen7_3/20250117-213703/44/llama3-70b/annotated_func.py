#State of the program right berfore the function call: The input is a list of vectors represented as (x, y) coordinates, where each vector starts at the origin. The length of the list is an integer n such that 2 ≤ n ≤ 100 000, and each vector is represented by a tuple (x_i, y_i) where |x_i|, |y_i| ≤ 10 000 and x_i^2 + y_i^2 > 0. No two vectors have the same direction, but they may have opposite directions.
def func():
    n = int(input())

v = []
    for _ in range(n):
        x, y = map(int, input().split())
        
        v.append((x, y))
        
    #State of the program after the  for loop has been executed: Output State: n is greater than 0, x is an integer, y is an integer, v is a list containing n tuples (x, y). The loop executes exactly n times, appending a new tuple (x, y) to the list v in each iteration.
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
        
    #State of the program after the  for loop has been executed: n is greater than 0, i is n-1, j is the index such that (i, j) gives the minimum angle, ans_angle is the minimum angle found, and ans is the tuple (i, j) with the smallest angle.
    print(ans[0] + 1, ans[1] + 1)
#Overall this is what the function does:The function accepts a list of vectors represented as (x, y) coordinates and finds a pair of vectors with the smallest angle between them. It first reads the number of vectors `n` and then reads each vector's coordinates. After sorting the vectors based on their polar angles, it iterates through the list to find the pair of vectors with the smallest angle. If multiple pairs have the same smallest angle, it returns the first pair found. The function prints the indices (1-based) of these two vectors. The function does not return a value directly but prints the result. Edge cases include handling a list with only two vectors and ensuring that the angle calculations are accurate even when vectors are very close to being collinear.

