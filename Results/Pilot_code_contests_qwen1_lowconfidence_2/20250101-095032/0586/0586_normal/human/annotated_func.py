#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n ≤ 100 and 1 ≤ k ≤ 10. The list `a` contains n positive integers each between 1 and 100 inclusive, representing the tastes of the fruits. The list `b` contains n positive integers each between 1 and 100 inclusive, representing the calories of the fruits.
def func():
    n, k = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())
    dp1 = defaultdict(lambda : 0, {(0): 0})
    pos = 0
    for (a, b) in zip(A, B):
        cur = a - b * k
        
        dp2 = dp1.copy()
        
        for x, y in dp1.iteritems():
            dp2[x + cur] = max(dp2[x + cur], y + a)
        
        dp1 = dp2
        
    #State of the program after the  for loop has been executed: 
    if (dp1[0] > 0) :
        print(dp1[0])
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`dp1` is a list of integers. If `dp1[0]` is greater than 0, the value of `dp1[0]` is printed. If `dp1[0]` is not greater than 0, -1 is printed.
#Overall this is what the function does:The function `func` accepts two parameters `n` and `k`, where `1 ≤ n ≤ 100` and `1 ≤ k ≤ 10`, along with two lists `a` and `b` containing `n` positive integers each between 1 and 100 inclusive, representing the tastes and calories of the fruits, respectively. The function calculates a dynamic programming solution to find the maximum possible taste difference (`taste - calorie*k`) that can be achieved by selecting a subset of fruits such that the total calorie does not exceed zero. If such a subset exists, the function prints the maximum taste difference; otherwise, it prints -1.

