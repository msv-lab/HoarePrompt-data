#State of the program right berfore the function call: The function should accept two parameters, n and k, where n is an integer such that 1 ≤ n ≤ 2 · 10^5, and k is an integer such that 1 ≤ k ≤ 10^9. These parameters represent the number of non-negative integers to be printed and their sum, respectively.
def func():
    for _ in range(int(input())):
        l1 = input().split()
        
        n, k = list(map(int, l1))
        
        if n == 1:
            print(k)
        else:
            arr = []
            k0 = k
            i = 0
            ans = []
            temp = 1
            while True:
                if temp * 2 < k:
                    temp *= 2
                    i += 1
                else:
                    break
            ans.append((1 << i) - 1)
            ans.append(k - sum(ans))
            ans += [0] * (n - len(ans))
            print(*ans)
        
    #State: The loop will print a sequence of non-negative integers for each test case. For each test case, if n is 1, it will print k. Otherwise, it will print a sequence of n integers where the first integer is the largest power of 2 less than k, the second integer is the difference between k and the first integer, and the remaining n-2 integers are 0.
#Overall this is what the function does:The function reads input from the user, processes multiple test cases, and for each test case, it prints a sequence of `n` non-negative integers that sum up to `k`. If `n` is 1, it prints `k`. Otherwise, it prints a sequence where the first integer is the largest power of 2 less than `k`, the second integer is the difference between `k` and the first integer, and the remaining `n-2` integers are 0.

