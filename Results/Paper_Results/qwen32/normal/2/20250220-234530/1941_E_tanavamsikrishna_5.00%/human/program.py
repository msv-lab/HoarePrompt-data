from typing import List
 
 
def best_solution(row: List[int], d: int):
    for i in range(0, d - 1):
        row[i] = row[i] + 1
    for i in range(d - 1, len(row)):
        row[i] = (min(row[max(0, i - (d + 1)) : i]) if i > 0 else 0) + row[i] + 1
    return row[-1]
 
 
def solve():
    n, m, k, d = (int(e) for e in input().split(" "))
    rows = [[int(e) for e in input().split(" ")] for _ in range(n)]
    costs = [best_solution(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i : i + k]))
    print(min(total_costs))
 
 
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()