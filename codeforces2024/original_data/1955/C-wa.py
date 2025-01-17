t = int(input()); from collections import deque;
for _ in range (t):
    n, k = map(int, input().split())
    lit = deque(list((map(int, input().split()))));
    lastState = -1; sunk = 0;
    while True:
        if len(lit) == 0 or k <= 0:
            break;
        if lastState == -1:
            lastState = 0;
        else:
            lastState = -1;
        u = lit[lastState];
        if u <= k:
            sunk += 1;
            if lastState == -1:
                lit.pop();
            else:
                lit.popleft();
        k -= u;
    print (sunk);