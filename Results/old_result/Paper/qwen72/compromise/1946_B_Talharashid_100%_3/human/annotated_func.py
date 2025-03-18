#State of the program right berfore the function call: The function `func` is expected to take input parameters, but they are not defined in the provided function definition. Based on the problem description, the function should take three parameters: a list of integers `a`, an integer `n` representing the length of the list `a`, and an integer `k` representing the number of operations. The list `a` contains integers within the range -10^9 to 10^9, and `n` and `k` are within the range 1 to 2 \cdot 10^5. Additionally, the function should handle multiple test cases, indicated by an integer `t` (1 \le t \le 10^4).
def func():
    for i in range(int(input())):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        c = 0
        
        maxi = 0
        
        for ele in l:
            if ele < 0 and c <= abs(ele):
                maxi = max(c, maxi)
                c = 0
            else:
                c += ele
                maxi = max(c, maxi)
        
        maxi = max(c, maxi)
        
        print((2 ** k * maxi - maxi + sum(l)) % 1000000007)
        
    #State: `i` is `t-1`, `n` and `k` are integers greater than 0, `l` is a list of integers input by the user, `c` is the sum of the non-negative subsequence of `l` that has the highest sum, and `maxi` is the maximum value of `c` observed during the loop execution, updated to be the maximum of the current `c` and the previous `maxi`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by a list of integers `l`, the length of the list `n`, and an integer `k` representing the number of operations. For each test case, it calculates the maximum sum of a contiguous subsequence of non-negative integers in `l`, and then computes a result based on this maximum sum, the number of operations `k`, and the total sum of the list `l`. The final result for each test case is printed, and it is the value of `(2

