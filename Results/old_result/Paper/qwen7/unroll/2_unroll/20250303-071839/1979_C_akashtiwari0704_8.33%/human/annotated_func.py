#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50. Additionally, k_i is an integer such that 2 ≤ k_i ≤ 20 for each outcome i.
def func():
    t = int(input())
    for T in range(t):
        bets = int(input())
        
        a = [int(x) for x in input().split()]
        
        prod = 1
        
        for i in range(bets):
            prod *= a[i]
        
        sumo = 0
        
        for i in range(bets):
            a[i] = prod // a[i]
            sumo += int(a[i])
        
        if sumo >= prod:
            print(-1)
        else:
            ans = ''
            for i in range(bets):
                ans += str(a[i]) + ' '
            print(ans)
        
    #State: Output State: The output state will consist of multiple lines, each corresponding to one iteration of the outer loop. For each line, there will be either a `-1` printed if the condition `sumo >= prod` is met, or a sequence of integers separated by spaces representing the transformed list `a` after applying the operations inside the loop. Each line will follow the format of the output produced within the loop's body.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t`, followed by `t` lines of input, each containing an integer `bets`. It then reads `bets` integers into a list `a`. The function calculates the product of all integers in `a` and divides each element in `a` by this product, summing these divisions. If the sum is greater than or equal to the product, it prints `-1`; otherwise, it prints the modified list `a` as space-separated integers. This process is repeated for each test case, producing a series of outputs corresponding to each test case.

