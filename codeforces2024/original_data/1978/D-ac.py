for _ in range (int(input())):
    pref = [0]; sm = [0];
    n, d = map(int, input().split())
    lit = list(map(int, input().split()));
    for i in range (n):
        pref.append(pref[-1]+lit[i]);
        sm.append(max(sm[-1], lit[n-i-1]));
    sm = list(reversed(sm));
    ans = [float('inf')];
    u = max(lit); idx = lit.index(u)+1;
    for i in range (1, n+1):
        if lit[i-1] == u:
            if lit[i-1] > lit[0] + d:
                if i == idx:
                    ans.append(0);
                else:
                    ans.append(i-1);
            else:
                ans.append(i-1); 
        else:
            if pref[i] + d >= sm[i]:
                ans.append(i-1);
            else:
                ans.append(i);
    print (' '.join(list(map(str, ans[1:]))));