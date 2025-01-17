def main():
    solve()


def solve():
    [n, m, q] = [int(i) for i in input().split(" ")]
    # 2 <= m <= n <= 3*10^5
    # 1 <= q <= 3*10^5
    X = [int(i) for i in input().split(" ")] # m
    V = [int(i) for i in input().split(" ")] # m

    ships = [0]
    j = 1
    # . . . . .
    # ^   ^   ^
    #   
    for i in range(1, n):
        if X[j] == i + 1:
            ships.append(0)
            j += 1
        else:
            ships.append((V[j - 1] * (X[j] - (i + 1)), X[j] - 1, V[j - 1]))

    #print(ships)
    for i in range(q):
        [c, x, v] = [int(i) for i in input().split(" ")]
        if c == 1:
            # add harbor >>
            x -= 1 # from 1 based to 0
            ships[x] = 0
            for i in range(x + 1, n):
                if ships[i] == 0:
                    break
                [_, j, _] = ships[i]
                ships[i] = ((j - i) * v, j, v)
            # add harbor <<
            for i in range(x - 1, -1, -1):
                if ships[i] == 0:
                    break
                [_, _, val] = ships[i]
                ships[i] = (val * (x - i), x, val)
        if c == 2:
            # output cost
            l, r = x, v 
            s = 0
            for i in range(l - 1, r):
                s += ships[i][0] if isinstance(ships[i], tuple) else 0
            print(s)
    #print(ships)

if __name__ == "__main__":
    main()