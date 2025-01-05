#State of the program right berfore the function call: H and W are positive integers such that 1 <= H, W <= 1000; C_h, C_w, D_h, and D_w are positive integers such that 1 <= C_h, D_h <= H and 1 <= C_w, D_w <= W; S is a 2D list of characters where each character is either '#' or '.', and S[C_h-1][C_w-1] and S[D_h-1][D_w-1] are '.'; (C_h, C_w) is not equal to (D_h, D_w).
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
        
    #State of the program after the  for loop has been executed: `h` is an input integer greater than 0, `w` is an input integer, `rows` is equal to `h`, `cols` is equal to `w`, `OK` is '.', `NG` is '#', `ns` is a defaultdict of sets, `ss` is a list of length `h` where each `ss[i]` is equal to the corresponding input string for all `i` from 0 to `h-1`.
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
        
    #State of the program after the  for loop has been executed: `goal` is equal to `dh * w + dw`, `seen` is a list of None values of length `n` with `seen[start]` set to 0, `q` is assigned the value `[(0, start)]`, `dx` contains `[-2, -2, -2, -2, -1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]`, `dy` contains `[-2, -1, -2, -1, -2, -1, 1, 2, -2, -1, 1, 2, -2, -1, 1, 2]`, and `vvs` contains values based on the evaluations of `abs(i) + abs(j)` for each combination.
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
        
    #State of the program after the loop has been executed: `seen` contains the minimum number of steps to reach each valid position represented by `u`, where `u` is calculated as `x * w + y` for all valid `x` and `y` derived from the offsets in `dx` and `dy`; `q` is empty; if `pu` equals `goal`, the loop has exited successfully; if there are any unreachable positions, `seen` reflects that with `None` values; if all positions are reachable, `seen` is updated accordingly.
    val = seen[goal]
    if (val is None) :
        print(-1)
    else :
        print(val)
    #State of the program after the if-else block has been executed: *`seen` contains the minimum number of steps to reach each valid position. If `val` is None, -1 is printed. Otherwise, if `val` is a valid number of steps (not None), then `val` is printed.
#Overall this is what the function does:The function accepts two positive integers representing the height (H) and width (W) of a grid, along with starting (C_h, C_w) and destination (D_h, D_w) coordinates. It processes a 2D grid of characters where each cell is either passable ('.') or blocked ('#'). The function calculates the minimum number of steps required to reach the destination from the starting point using valid moves, considering both single-step and double-step movements. If the destination is unreachable, it returns -1. If reachable, it returns the minimum number of steps.

