def func_1(n, m, k):
    if k < n - 1:
        print(k + 1, 1)
    else:
        k -= n - 1
        full_rows = k // (m - 1)
        remaining_steps = k % (m - 1)
        if full_rows % 2 == 0:
            row = n - full_rows
            col = 2 + remaining_steps
        else:
            row = n - full_rows
            col = m - remaining_steps
        print(row, col)
input = sys.stdin.read
data = input().strip().split()
(n, m, k) = (int(data[0]), int(data[1]), int(data[2]))
func_1(n, m, k)