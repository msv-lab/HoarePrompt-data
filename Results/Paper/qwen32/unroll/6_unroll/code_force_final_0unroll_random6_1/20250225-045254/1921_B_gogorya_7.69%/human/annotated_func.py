#State of the program right berfore the function call: Each test case consists of three lines. The first line contains a single integer n (1 ≤ n ≤ 10^5) — the number of boxes. The second line contains a string s of n characters, where the i-th character is '1' if there is a cat in the i-th box and '0' otherwise. The third line contains a string f of n characters, where the i-th character is '1' if there should be a cat in the i-th box and '0' otherwise. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s1 = input()
        
        s2 = input()
        
        a1 = s1.count('1')
        
        a2 = s2.count('1')
        
        hd = a1 - a2
        
        res = abs(a1 - a2)
        
        for i in range(n):
            if hd > 0:
                hd -= 1
                continue
            if s1[i] == '1' and s2[i] == '0':
                res += 1
        
        print(res)
        
    #State: a list of `t` integers, where each integer represents the number of moves required to adjust the cat arrangement in the boxes from `s1` to `s2` for each of the `t` iterations.
#Overall this is what the function does:The function reads multiple test cases, each consisting of the number of boxes `n`, the initial cat arrangement `s1`, and the desired cat arrangement `s2`. For each test case, it calculates and prints the minimum number of moves required to adjust the cat arrangement in the boxes from `s1` to `s2`.

