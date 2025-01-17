N,M = map(int, input().split())
field = [input().split() for _ in range(N)]
assert all(len(row)==M for row in field)
pos = {
    ent: [r,c] for r,row in enumerate(field) for c,ent in enumerate(row)
    if ent not in ["..", "RG", "BG"]
}
score = [0,0]
T = int(input())
for t in range(T):
    ent, arg, *opt = input().split()
    if arg in "UDLR":
        d = "UDLR".index(arg)
        pos[ent][d//2] += [-1,+1][d%2]
        elim = sorted(ent for ent in pos if ent[0]!="." and pos[ent]==pos.get(".B"))
        for ent in elim:
            print(t, ent, "ELIMINATED")
            del pos[ent]
    elif arg =="T":
        r,c = pos[ent]
        g = field[r][c]
        if g[1] == "G":
            d = "BR".index(g[0])
            print(t, ["RED", "BLUE"][d], "GOAL")
            score[d] += 1
    else:
        assert arg == "C"
        [opt] = opt
        if opt == ".S":
            d = "RG".index(ent[0])
            print(t, ["RED", "BLUE"][d], "CATCH GOLDEN SNITCH")
            score[d] += 10
print("FINAL SCORE:", *score)