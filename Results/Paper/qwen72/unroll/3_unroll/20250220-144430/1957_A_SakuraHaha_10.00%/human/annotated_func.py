#State of the program right berfore the function call: The function should take three parameters: t, a list of integers n, and a list of lists a, where t is the number of test cases (1 ≤ t ≤ 100), each n[i] is the number of sticks for the i-th test case (1 ≤ n[i] ≤ 100), and each a[i] is a list of stick lengths for the i-th test case, with each stick length a[i][j] being an integer (1 ≤ a[i][j] ≤ 100).
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: `t` remains the number of test cases (1 ≤ t ≤ 100), `n` remains the input integer, `a` remains the list of integers where each element a[j] is an integer (1 ≤ a[j] ≤ 100), `ans` remains 0, `cnt` is a dictionary where each key is an integer from the list `a` and each value is the count of how many times that integer appears in `a`.
    for x in cnt.values():
        ans += x // 4
        
    #State: `t` remains the number of test cases (1 ≤ t ≤ 100), `n` remains the input integer, `a` remains the list of integers where each element a[j] is an integer (1 ≤ a[j] ≤ 100), `ans` is the sum of the floor division of each value in `cnt` by 4, `cnt` remains a dictionary where each key is an integer from the list `a` and each value is the count of how many times that integer appears in `a`.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the sum of the floor division of each count in `cnt` by 4.
    #   - Since the exact list `a` is not provided, we can't compute the exact numerical value of `ans`. However, based on the structure of the problem, the print statement will output the calculated value of `ans`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` takes no parameters and reads input from the user. It processes a list of integers `a` by counting the occurrences of each integer and then calculates the sum of the floor division of each count by 4. The function prints this sum as the final output. The function does not return any value.

