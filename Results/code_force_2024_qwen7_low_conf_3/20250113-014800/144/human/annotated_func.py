#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        z = 0
        
        for i in range(n):
            if a[a[i] - 1] == i + 1:
                z = 1
                break
        
        if z == 0:
            print(3)
        else:
            print(2)
        
    #State of the program after the  for loop has been executed: `user_input` is an integer greater than 0, `t` is 0, `n` is the last input integer received, `a` is a list of integers obtained from the last user's input, `z` is 1 if the condition `a[a[i] - 1] == i + 1` is true for any index `i` in the range [0, n-1], otherwise `z` is 0. If `z` is 0, the number 3 is printed. If `z` is 1, the number 2 is printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of length `n`. It then checks if there exists an index `i` such that `a[a[i] - 1] == i + 1`. If such an index exists, the function prints `2`; otherwise, it prints `3`. The function iterates through all test cases provided in `t`. After completing the processing of all test cases, the function does not return anything explicitly (it only prints the results during execution). Potential edge cases include invalid inputs (e.g., non-integer values for `t` or `n`, or values outside the specified ranges), but the provided code handles these by using `int(input())` which will raise a `ValueError` for non-integer inputs. The final state of the program is that it has processed all test cases and printed the results accordingly.

