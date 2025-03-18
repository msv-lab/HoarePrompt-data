#State of the program right berfore the function call: The function should take a list of test cases, where each test case is a list containing an integer n followed by a list of n integers representing the lengths of the sticks. Each test case list should be structured as [n, [a_1, a_2, ..., a_n]], with 1 <= t <= 100, 1 <= n <= 100, and 1 <= a_i <= 100.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: `ans` is 0, `cnt` is a dictionary where each key is a unique integer from the list `a` and the value is the count of how many times that integer appears in `a`, `a` is a list of integers that must have at least `n` elements, where `n` is the length of the list `a`.
    for x in cnt.values():
        ans += x // 4
        
    #State: `ans` is the sum of `x // 4` for each value `x` in `cnt.values()`, `cnt` remains a dictionary where each key is a unique integer from the list `a` and the value is the count of how many times that integer appears in `a`.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the sum of `x // 4` for each value `x` in `cnt.values()`.
    #   - Since the exact list `a` is not provided, we can't compute the exact numerical value of `ans`. However, based on the structure of the problem, the print statement will output the calculated sum of `x // 4` for each count `x` in `cnt`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of `n` integers from the user input. It then counts the occurrences of each integer in the list and calculates the sum of the integer counts divided by 4 (using integer division). Finally, it prints this sum. The function does not return any value.

