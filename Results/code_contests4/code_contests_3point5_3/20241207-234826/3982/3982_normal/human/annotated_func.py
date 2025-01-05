#State of the program right berfore the function call: **
def func_1():
    n, m = func_2()
    robbers = func_4(n, 2)
    lights = func_4(m, 2)
    rel_lights_x = []
    rel_lights_y = []
    for (rx, ry) in robbers:
        for lx, ly in lights:
            x, y = lx - rx, ly - ry
            if x >= 0 and y >= 0:
                rel_lights_x.append(x)
                rel_lights_y.append(y)
        
    #State of the program after the  for loop has been executed: `rel_lights_x` contains all non-negative x-coordinate differences between lights and robbers, `rel_lights_y` contains all non-negative y-coordinate differences between lights and robbers, `robbers` list has been fully iterated through, `lights` list has been fully iterated through, all possible non-negative differences between the coordinates have been appended to `rel_lights_x` and `rel_lights_y`, `lx` is the x-coordinate of the last element in the lights list, `ly` is the y-coordinate of the last element in the lights list, x is greater than or equal to 0, y is greater than or equal to 0
    n = len(rel_lights_x)
    l, r = 0, 10 ** 6 + 1
    avail = [0] * (10 ** 6 + 1 + 1)
    while l < r:
        ans = l + (r - l) // 2
        
        for i in range(ans + 1):
            avail[i] = 0
        
        for i in range(n):
            x = rel_lights_x[i]
            y = rel_lights_y[i]
            if x + y >= ans:
                sp = max(0, x - (x + y - ans))
                ep = min(ans, x)
                avail[sp] += 1
                if ep < ans:
                    avail[ep + 1] -= 1
        
        psum_min = INF
        
        psum = 0
        
        for ax in avail:
            psum += ax
            psum_min = min(psum_min, psum)
        
        if psum_min == 0:
            r = ans
        else:
            l = ans + 1
        
    #State of the program after the loop has been executed: After the loop executes, `psum_min` is the minimum value among all the partial sums in `avail`, `psum` is the sum of all elements in `avail`, `avail` list has all its elements processed, `ax` is the last element in the `avail` list. If `psum_min` is equal to 0, `r` is assigned the value of `ans`. If `psum_min` is not equal to 0, `l` is set to `ans + 1`. Additionally, `l` is no longer less than `r` as the loop condition is false.
    print(l)
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any value. It iterates through the lists of robbers and lights, calculates the differences in coordinates, and then performs a binary search algorithm to find a specific value. The function prints the final value of `l` after the binary search loop.

#State of the program right berfore the function call: **
def func_2():
    return [int(x) for x in input().split()]
    #The program returns a list of integers obtained by converting each element x from the input split by spaces to an integer
#Overall this is what the function does:The function func_2 does not accept any parameters. It reads input from the user, splits the input by spaces, converts each element to an integer, and returns a list of these integers.

#State of the program right berfore the function call: **Precondition**: 
- n and m are integers such that 1 ≤ n, m ≤ 2000.
- For each robber i, a_i and b_i are integers such that 0 ≤ a_i, b_i ≤ 10^6.
- For each searchlight j, c_j and d_j are integers such that 0 ≤ c_j, d_j ≤ 10^6.
def func_3(o):
    return [(int(x) + o) for x in input().split()]
    #The program returns a list of integers where each element is obtained by adding 'o' to the integer value of each element x in the input string split by spaces.
#Overall this is what the function does:The function func_3 accepts a parameter `o` and returns a list of integers where each element is obtained by adding `o` to the integer value of each element `x` in the input string split by spaces. The code does what the annotations describe, with no missing functionality or edge cases mentioned.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 2000. The coordinates a_i, b_i, c_i, d_i are integers such that 0 ≤ a_i, b_i, c_i, d_i ≤ 10^6 for 1 ≤ i ≤ n and 1 ≤ i ≤ m.**
def func_4(n, m):
    return [func_2() for _ in range(n)]
    #The program returns a list of length n, where each element is the result of calling func_2()
#Overall this is what the function does:The function func_4 accepts two integer parameters n and m, and returns a list of length n, where each element is the result of calling func_2(). The function assumes func_2() exists and can be called successfully.

#State of the program right berfore the function call: **Precondition**: **n and m are positive integers such that 1 ≤ n, m ≤ 2000. The coordinates of robbers and searchlights are non-negative integers less than or equal to 10^6.**
def func_5(f):
    return [func_5(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    #The program returns a list of values obtained by calling function func_5 with arguments *dim[1:] for dim[0] times if dim is not empty, otherwise it returns the result of calling function f()
#Overall this is what the function does:The function func_5 accepts a parameter f and returns a list of values obtained by recursively calling func_5 with arguments dim[1:] for dim[0] times if dim is not empty. If dim is empty, the function directly returns the result of calling function f(). The function operates recursively based on the provided conditions.

