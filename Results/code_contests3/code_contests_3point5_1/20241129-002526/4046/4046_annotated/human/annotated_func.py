#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^9).**
def func():
    n = int(input())
    l, ans = len(str(n)), 4444477777
    if (l & 1) :
        l += 1
    #State of the program after the if block has been executed: *n is a positive integer, l is the length of n. If the length of n is odd, l is increased by 1 (making it even), and ans remains 4444477777. Otherwise, there is no change in the values of n, l, and ans.
    for i in range(l, 10, 2):
        for x in product('74', repeat=i):
            if x.count('7') == x.count('4'):
                tem = int(''.join(x))
                if tem >= n:
                    ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `n` remains a positive odd integer, `l` remains the next even number less than the current value of `l + 2`, `ans` retains the minimum value between the current value of `ans` and `tem`, `x` is based on the product('74', repeat=i) where i is the next even number less than `l + 2`, the count of '7' in `x` is equal to the count of '4' in `x`, and `tem` is greater than or equal to `n`.
    print(ans)
#Overall this is what the function does:The `func` function reads an integer `n` from the user input, calculates the length `l` of `n`, and adjusts `l` to be even if it is odd. Then, it iterates through combinations of '7's and '4's of increasing length starting from `l` up to 10. For each combination, if the count of '7's is equal to the count of '4's and the formed number is greater than or equal to `n`, it updates `ans` to be the minimum value between the current `ans` and the formed number. Finally, it prints the minimum `ans` value found during the iteration. However, the functionality of the function is incomplete as it lacks clear postconditions and returns.

