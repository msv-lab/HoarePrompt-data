#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:45:43 2024

@author: wangyiyang
"""

import queue
T = int(input())

def solve():
    n,m = [int(x) for x in input().split(' ')]
    s = [[0 for j in range(m + 5)]for i in range(n + 5)]
    for i in range(0,n):
        s[i] = [int(x) for x in input().split(' ')]
    vis = [[0 for j in range(m + 5)]for i in range(n + 5)]
    class Q:
        def __init__(self,x,y,d,d_down):
            self.x = x
            self.y = y
            self.d = d
            self.d_down = d_down
    ans = 10**9
    q = queue.Queue()
    Point = Q(0,0,0,0)
    q.put(Point)
    while (q.empty() == False):
        u = q.get()
        ux = u.x
        uy = u.y
        ud = u.d 
        udown = u.d_down
        tx = (ux + 2) % n
        ty = uy
        if(tx >= 0 and tx < n and ty < m and ty >= 0 and s[tx][ty] == 0):
            if(ty == m - 1):
                now = (udown + 1) % n
                ans = min(ans , ud + 1 + min(now + 1 , n - now - 1))
            else:
                if(vis[tx][ty] == 0):
                    q.put(Q(tx,ty,ud + 1,udown + 1))
                    vis[tx][ty] = 1
        tx = (ux + 1) % n
        ty = uy + 1
        if(tx >= 0 and tx < n and ty < m and ty >= 0 and s[tx][ty] == 0):
            if(ty == m - 1):
                now = (udown) % n
                ans = min(ans , ud + 1 + min(now + 1 , n - now - 1))
            else:
                if(vis[tx][ty] == 0):
                    q.put(Q(tx,ty,ud + 1,udown))
                    vis[tx][ty] = 1
    if(ans == 10**9):
        print(-1)
    else:
        print(ans)
    
for q in range(0,T):
    solve()