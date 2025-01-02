#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and k is a positive integer such that 1 <= k <= 10. The list a contains n positive integers each between 1 and 100, inclusive, representing the tastes of the fruits. The list b contains n positive integers each between 1 and 100, inclusive, representing the calories of the fruits.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer, `k` is an integer, `a` is a list of `n` positive integers, `B` is a list of `n` integers, `dp1` is a dictionary with keys as integers and values as integers, `pos` is 0, `dp1` is updated to reflect the maximum values obtained by iterating through `a` and `B` using the defined process.
    if (dp1[0] > 0) :
        print(dp1[0])
    else :
        print(-1)
    #State of the program after the if-else block has been executed: `n` is an integer, `k` is an integer, `a` is a list of `n` positive integers, `B` is a list of `n` integers, `dp1` is a dictionary with keys as integers and values as integers, `pos` is 0. If `dp1[0]` is greater than 0, the function reflects the maximum values obtained by iterating through `a` and `B` using the defined process, and does not print anything. Otherwise, `dp1` is updated to reflect the maximum values obtained by iterating through `a` and `B` using the defined process, and `-1` is printed.
#Overall this is what the function does:The function processes two lists, `A` and `B`, containing `n` positive integers each, and an integer `k`. It calculates the maximum sum of elements from list `A` such that the corresponding elements in list `B` do not exceed `k` when multiplied. This is achieved using dynamic programming stored in the dictionary `dp1`. After processing, the function prints the maximum sum if it is greater than 0; otherwise, it prints `-1`. The function does not return any value. Edge cases include when `dp1[0]` is not updated properly or when the input lists `A` and `B` contain invalid values (though the code assumes valid inputs based on the given constraints).

