#State of the program right berfore the function call: **
def func():
    input = lambda : sys.stdin.readline().rstrip()
    sys.setrecursionlimit(max(1000, 10 ** 9))
    write = lambda x: sys.stdout.write(x + '\n')
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    ch -= 1
    cw -= 1
    dh -= 1
    dw -= 1
    rows, cols = h, w
    OK = '.'
    NG = '#'
    ns = defaultdict(set)
    ss = [None] * rows
    for i in range(rows):
        s = input()
        
        ss[i] = s
        
    #State of the program after the  for loop has been executed: `dh` is decremented by 2, `dw` is unknown, `ch` is decremented by 1, `cw` is decreased by 1, `rows` is assigned the value of `h`, `cols` is assigned the value of `w`, `OK` is '.', `NG` is '#', `ns` is a defaultdict of sets, `ss` is a list where `ss[i]` is assigned the value of `s`, `rows` is greater than 0, `i` is equal to `rows - 1`, `s` is the input string
    n = rows * cols
    start = ch * w + cw
    goal = dh * w + dw
    seen = [None] * n
    seen[start] = 0
    q = [(0, start)]
    dx = []
    dy = []
    vvs = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if not i == j == 0:
                dx.append(i)
                dy.append(j)
                if abs(i) + abs(j) > 1:
                    vvs.append(1)
                else:
                    vvs.append(0)
        
    #State of the program after the  for loop has been executed: `vvs` is a list containing either 1 or 0 based on the conditions, `i` is 2, `j` is 2, `dx` is [-2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2], `dy` is [2, -2, 3, 3, 1, next_j, j, 1, 3, 0, 2, -2, 3, 3, 1, next_j, j, 1, 3, 0] or [2, -2, 3, 3, 1, next_j, j, 1, 3, 0, 2, -2, 3, 3, 1, next_j, j, 1, 3, 0] depending on the condition
    while q:
        pnum, pu = hpp(q)
        
        ux, uy = divmod(pu, w)
        
        if pu == goal:
            break
        
        for xx, yy, vv in zip(dx, dy, vvs):
            x, y = ux + xx, uy + yy
            u = x * w + y
            num = pnum + vv
            if x < 0 or y < 0 or x >= h or y >= w or ss[x][y] == '#':
                continue
            if seen[u] is None or seen[u] > num:
                seen[u] = num
                hp(q, (num, u))
        
    #State of the program after the loop has been executed: After the loop executes, the variables `u`, `num`, `x`, `y`, `h`, `w`, `ss`, `pnum`, `vv`, `dx`, `dy`, `vvs`, `seen`, and `q` will have specific values based on the conditions within the loop. The loop will update `seen[u]` with the minimum value of `num` encountered during the loop iterations. If `pu` is equal to `goal`, the loop will break. Additionally, the loop control variable `q` will be False, indicating the end of the loop.
    val = seen[goal]
    if (val is None) :
        print(-1)
    else :
        print(val)
    #State of the program after the if-else block has been executed: *`val` is assigned the value of `seen[goal]`. If `val` is None, then `val` is assigned the value of `seen[goal]` and -1 is printed. Otherwise, `val` retains the value of `seen[goal]`.
#Overall this is what the function does:The function `func` reads input about a grid and two points, performs a pathfinding algorithm on the grid to find the shortest path from one point to another, and then prints the length of the shortest path. It does not accept any parameters and does not return any value. If the algorithm fails to find a path (value is None), it prints -1.

