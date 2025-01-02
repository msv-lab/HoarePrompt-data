#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 105. The list of integers a has length n, and each element ai satisfies 1 ≤ ai ≤ 105.
def func():
    n, k = map(int, raw_input().split())
    ls = map(int, raw_input().split())
    tmp = ls[k - 1]
    check = True
    for i in range(k, n):
        if ls[i] != tmp:
            check = False
        
    #State of the program after the  for loop has been executed: `n` and `k` are integers such that 1 ≤ k ≤ n ≤ 105, the list `a` has length `n`, and each element `ai` satisfies 1 ≤ ai ≤ 105; `ls` is a list of integers with length `n` where each element is between 1 and 105; `tmp` is the integer value of `ls[k - 1]`. After the loop, `check` is `True` if all elements in `ls` from index `k` to `n-1` are equal to `tmp`, otherwise `check` is `False`.
    if check :
        print(k - 1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`n` and `k` are integers such that 1 ≤ k ≤ n ≤ 105, the list `a` has length `n`, and each element `ai` satisfies 1 ≤ ai ≤ 105; `ls` is a list of integers with length `n` where each element is between 1 and 105; `tmp` is the integer value of `ls[k - 1]`. After the loop, `check` is `True` if all elements in `ls` from index `k` to `n-1` are equal to `tmp`, otherwise `check` is `False`. If `check` is `True`, the value `k - 1` has been printed. If `check` is `False`, it indicates that not all elements in `ls` from index `k` to `n-1` are equal to `tmp`.
#Overall this is what the function does:The function reads two integers `n` and `k` from the input, followed by a list of `n` integers `ls`. It then checks if all elements in `ls` from index `k` to `n-1` are equal to the element at index `k-1`. If this condition is met, the function prints `k - 1`; otherwise, it prints `-1`. The function does not return any value but modifies the program state by printing one of the two values. The function assumes that `1 ≤ k ≤ n ≤ 105` and each element `ai` in `ls` satisfies `1 ≤ ai ≤ 105`. Potential edge cases include when `k` is 1 (meaning the entire list is checked) or when `k` is `n` (meaning no elements are checked beyond the initial one). If the input does not meet the expected constraints, the behavior of the function is undefined.

