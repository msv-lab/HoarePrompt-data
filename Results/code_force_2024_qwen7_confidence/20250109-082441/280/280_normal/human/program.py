n, t = map(int, input().split());

from collections import defaultdict

def compare(a, b):
    return False if a == b and b == True else True;

adj = defaultdict(list);

for i in range (n-1):
    x, y = map(int, input().split());
    adj[x].append(y); adj[y].append(x);

dp = [True for _ in range (n+1)];

vis = [False for _ in range (n+1)];

def dfs(idx):
    if len(adj[idx]) == 0:
        dp[idx] = False;
        return;
    vis[idx] = True;
    for i in adj[idx]:
        if not vis[i]:
            dfs(i);
            dp[idx] = compare(dp[i], dp[idx]);

t = int(input());
dfs(t);
if (dp[t]): print ("Ron");
else: print ("Hermione")