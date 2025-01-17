#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2⋅10^5, and a is a list of n integers where 0 ≤ a_i ≤ n for each 1 ≤ i ≤ n.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    positions = []
    for i in range(n):
        positions.append((i + 1, i + 1))
        
    #State of the program after the  for loop has been executed: `n` is an integer where \(2 \leq n \leq 2 \cdot 10^5\), `a` is a list of `n` integers where \(0 \leq a_i \leq n\) for each \(1 \leq i \leq n\), `positions` is a list containing \([(i+1, i+1) \text{ for } i \text{ in range}(n)]\), `i` is \(n-1\)
    visit = [-1] * n
    for i in range(n):
        found = False
        
        for j in range(n):
            if i != j:
                dist = abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] -
                    positions[j][1])
                if dist == a[i]:
                    visit[i] = j + 1
                    found = True
                    break
        
        if not found:
            print('NO')
            return
        
    #State of the program after the  for loop has been executed: Output State:
    print('YES')
    for pos in positions:
        print(pos[0], pos[1])
        
    #State of the program after the  for loop has been executed: `total'` is positive, `num` is negative, `x` is 0, `positions` is an empty list, no print statements have been executed.
    print(' '.join(map(str, visit)))
#Overall this is what the function does:The function processes a list of integers `a` of length `n`, where each element `a_i` represents the Manhattan distance between two points in a grid. It attempts to find a permutation of indices such that the Manhattan distance between the points corresponding to consecutive indices in the permutation matches the values in `a`. If such a permutation exists, the function prints "YES" followed by the positions of the points, and the visited indices (which indicate the mapping). If no valid permutation can be found, the function prints "NO". The function does not return any value.

