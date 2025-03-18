from heapq import heapify, heappop, heappush
 
 
def best_bridge_cost(row, d: int):
    row[0] = 1
    for i in range(1, d):
        row[i] = row[i] + 2
    min_heap = [(e, i) for i, e in enumerate(row[:d])]
    heapify(min_heap)
    for i in range(d, len(row)):
        while (e := heappop(min_heap))[1] <= i - (d + 2):
            pass
        row[i] = e[0] + row[i] + 1
        heappush(min_heap, e)
        heappush(min_heap, (row[i], i))
    return row[-1]
 
 
def solve():
    n, m, k, d = (int(e) for e in input().split(" "))
    rows = [[int(e) for e in input().split(" ")] for _ in range(n)]
    costs = [best_bridge_cost(row, d) for row in rows]
    total_costs = []
    for i in range(len(costs) - (k - 1)):
        total_costs.append(sum(costs[i : i + k]))
    print(min(total_costs))
 
 
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()