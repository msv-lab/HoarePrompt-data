#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers such that 1 ≤ n ≤ 3 · 10^5, 1 ≤ m ≤ 10^9, and 1 ≤ k ≤ min(nm, 10^9), representing the number of sale days, the maximum amount of tickets purchasable each day, and the total number of tickets to be bought, respectively. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, representing the price per ticket for each of the upcoming n days. The sum of n over all test cases does not exceed 3 · 10^5.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        s = 0
        
        c = k * k / 2
        
        for i in range(n):
            s = min(m, k)
            k -= s
            c += l[i] * s - s * s / 2
        
        print(int(c))
        
    #State: For each test case, the output is the integer value of `c`, which represents the total cost of buying `k` tickets, considering the minimum cost strategy. The loop iterates through the sorted list of ticket prices, `l`, and calculates the total cost by buying the maximum number of tickets possible each day, up to `m` tickets, until `k` tickets are bought. The variable `c` is updated to include the cost of tickets bought each day, adjusted by the formula `c += l[i] * s - s * s / 2`, where `s` is the number of tickets bought on day `i`. After all iterations, `c` is printed as an integer.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it takes the number of sale days `n`, the maximum number of tickets purchasable each day `m`, the total number of tickets to be bought `k`, and a list of ticket prices `a` for each day. It calculates and prints the minimum total cost required to buy `k` tickets over the `n` days, considering the maximum number of tickets that can be bought each day is `m`. The function does not return any value; it only prints the result for each test case. After processing all test cases, the function concludes.

