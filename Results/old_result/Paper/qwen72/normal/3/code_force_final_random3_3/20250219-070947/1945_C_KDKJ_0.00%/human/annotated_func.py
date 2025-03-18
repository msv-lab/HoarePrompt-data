#State of the program right berfore the function call: n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of '0' and '1'.
def func_1():
    n = int(input())
    a = input()
    S = [[0, 0]]
    for s in a:
        x, y = S[-1]
        
        if s == '0':
            x += 1
        else:
            y += 1
        
        S.append([x, y])
        
    #State: `n` is an input integer, `a` is a string consisting only of '0' and '1' provided by the user that must have at least `len(a)` characters, `S` is a list containing `len(a) + 1` sublists. Each sublist in `S` represents the cumulative count of '0's and '1's encountered in the string `a` up to that point. The final sublist in `S` will contain the total counts of '0's and '1's in the entire string `a`.
    ans = 0
    satisfy = 0
    for i in range(n):
        left = S[i][0]
        
        lsum = S[i][0] + S[i][1]
        
        right = S[-1][1] - S[i][1]
        
        rsum = n - lsum
        
        if left * 2 < lsum or right * 2 < rsum:
            continue
        elif abs(n / 2 - i) <= abs(n / 2 - ans):
            ans = i
        
    #State: `n` must be greater than 0, `i` is `n`, `a` is a string consisting only of '0' and '1' provided by the user that must have at least `len(a)` characters, `S` is a list containing `len(a) + 1` sublists, `satisfy` is 0, `ans` is the index `i` that minimizes the absolute difference between `n / 2` and `i` while satisfying the conditions `left * 2 >= lsum` and `right * 2 >= rsum` for each iteration.
    print(ans)
    #This is printed: - Since the exact values of `left`, `right`, `lsum`, and `rsum` are not provided, we cannot compute the exact numerical value of `ans`.
    #   - However, based on the given conditions, `ans` will be the index `i` that is closest to `n / 2` and satisfies the conditions `left * 2 >= lsum` and `right * 2 >= rsum`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a string `a` of length `n` consisting only of '0' and '1'. It computes and prints an index `ans` that represents the position in the string `a` where the cumulative counts of '0's and '1's on the left and right sides of the index meet specific balance conditions. Specifically, the index `ans` is chosen such that the number of '0's on the left side is at least half the total characters on the left, and the number of '1's on the right side is at least half the total characters on the right. The function prints the index `ans` that is closest to `n / 2` and satisfies these conditions. If no such index exists, the function will print the closest valid index to `n / 2`.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: `int(input())` must return a positive integer, `_` is `int(input()) - 1`, `func_1()` has been called `int(input())` times.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer from the user input, which must be a positive integer, and calls the function `func_1` that many times. After the function concludes, `func_1` has been called the number of times specified by the user input, and the program state is such that the input has been consumed and the side effects of `func_1` have been applied the specified number of times.

