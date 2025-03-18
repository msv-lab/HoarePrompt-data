#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50. The list k contains n positive integers such that 2 ≤ k_i ≤ 20.
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
        
    #State: The output will consist of multiple lines, each corresponding to one iteration of the outer loop. For each line, if the sum of the modified array (where each element is the product of all elements divided by the current element) is greater than or equal to the product of all elements, it will print -1. Otherwise, it will print the modified array elements separated by spaces. The exact values depend on the input provided for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `bets` and a list of `bets` positive integers `a`. For each test case, it calculates the product of all elements in `a`, then modifies each element to be the product of all elements divided by the current element. It computes the sum of these modified elements and compares it to the original product. If the sum is greater than or equal to the product, it prints `-1`; otherwise, it prints the modified elements as a space-separated string. The function handles up to 10,000 test cases, with each test case containing between 1 and 50 elements, where each element is between 2 and 20.

