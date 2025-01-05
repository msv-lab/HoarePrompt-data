mod = int(1000000000.0 + 7)

def func_1(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def func_2(a, b):
    return a * b % mod

def func_3(a, b):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return func_2(a, func_3(a, b - 1))
    else:
        temp = func_3(a, b / 2)
        return func_2(temp, temp)

def func_4(a):
    return func_3(a, mod - 2)

def func_5(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0
    return x

def func_6():
    n = int(raw_input())
    arr = [int(x) for x in raw_input().split()]
    answer = {}
    for i in range(n):
        cnt = {}
        x = arr[i]
        i = 2
        while i * i <= x:
            while x % i == 0:
                x /= i
                cnt[i] = cnt.get(i, 0) + 1
            i += 1
        if x != 1:
            cnt[x] = cnt.get(x, 0) + 1
        for key in cnt:
            answer[key] = max(answer.get(key, 0), cnt[key])
    lcm = 1
    for prime in answer:
        for _ in range(answer[prime]):
            lcm = func_2(lcm, prime)
    ans = 0
    for x in arr:
        ans = func_1(ans, func_2(lcm, func_4(x)))
    ans = int(ans)
    print(ans)
func_6()
'\n#include <bits/stdc++.h>\nusing namespace std;\n\nusing ll = long long; \nconst int MOD = 1e9+7;\n\nll add(ll a, ll b) {\n    return (a + b) % MOD;    \n}\n\nll divi(ll a, ll b) {\n    return (a / b) % MOD;\n}\n\nll mul(ll a, ll b) {\n    return (a * b) % MOD;\n}\n\n// Return a ^ b \nint my_pow(int a, int b) {\n    if (b == 0) {\n        return 1;\n    }\n    else if (b % 2 == 1) {\n        return mul(a, my_pow(a, b-1));\n    }\n    else {\n        int temp = my_pow(a, b/2);\n        return mul(temp, temp);\n    }\n}\n\nint my_inv(int a) {\n    return my_pow(a, MOD-2);\n}\n\nint main() {\n    int n;\n    \n    scanf("%d", &n);\n    \n    vector<int> arr(n);\n    \n    map<int, int> answer;\n    //cout << "test" << endl;\n    for (int i = 0; i < n; i++) {\n        map<int, int> cnt;        \n        scanf("%d", &arr[i]);\n        int x = arr[i];\n        \n        //cout << x << endl;\n        \n        for (int i = 2; i * i <= x; i++) {\n            while (x % i == 0) {\n                cnt[i] += 1;\n                x /= i;\n            }\n        }\n        \n        if (x != 1) {\n            cnt[x] += 1;\n        }\n        \n        //cout << "test_x" << endl;\n        \n        for (pair<int, int> p : cnt) {\n            answer[p.first] = max(answer[p.first], p.second);\n        }\n    }\n    //cout << "test2" << endl;\n    \n    ll lcm = 1;\n    for (pair<int, int> p : answer) {\n        int prime = p.first;\n        int k = p.second;\n        for (int i = 0; i < k; i++) {\n            lcm = mul(lcm, prime);\n        }\n    }\n    \n    ll ans = 0;\n    \n    //cout << "test1" << endl;\n    \n    for (int i = 0; i < n; i++) {\n        ans = add(ans, mul(lcm, my_inv(arr[i])));\n    }\n    \n    //cout << "test2" << endl;\n    \n    printf("%lld", ans);\n\t\n\treturn 0;\n}\n'