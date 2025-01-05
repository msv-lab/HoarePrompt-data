#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 200,000, and a list of n integers where each integer is either 0 or 1, representing the sequence of doors opened, with at least one 0 and one 1 in the list.
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `c` is a map object of integers converted from input, `ans` is the index of the last element in `c` that is different from its next element, or `ans` remains 0 if all elements in `c` are equal.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` and a list of `n` integers (0s and 1s), and prints the index of the last element that differs from its next element, or 0 if all elements are the same.

