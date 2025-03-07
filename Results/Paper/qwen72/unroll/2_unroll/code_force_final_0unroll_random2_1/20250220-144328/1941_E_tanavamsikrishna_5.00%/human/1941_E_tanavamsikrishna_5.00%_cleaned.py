def func_1(row: List[int], d: int):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)):i]) if i > 0 else 0) + row[i] + 1
    return row[-1]

def func_2():
    (n, m, k, d) = (int(e) for e in input().split(' '))
    rows = [[int(e) for e in input().split(' ')] for _ in range(n)]
    costs = [func_1(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i:i + k]))
    print(min(total_costs))
if __name__ == '__main__':
    for _ in range(int(input())):
        func_2()