#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, the function receives three integers k (2 ≤ k ≤ 30), x (1 ≤ x ≤ 100), and a (1 ≤ a ≤ 10^9) representing the number of times the bet is increased in case of a win, the maximum number of consecutive losses, and the initial number of coins Sasha has, respectively.
def func():
    t = int(input())
    for _ in range(t):
        k, x, a = map(int, input().split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 3:
                print('YES')
            else:
                print('NO')
        else:
            z = 0
            for i in range(x + 1):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: A sequence of 'YES' or 'NO' printed lines, one for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by three integers: `k` (the number of times the bet is increased in case of a win), `x` (the maximum number of consecutive losses), and `a` (the initial number of coins Sasha has). For each test case, it determines whether Sasha can continue playing the game without running out of coins based on the given conditions and prints 'YES' if possible, otherwise 'NO'.

