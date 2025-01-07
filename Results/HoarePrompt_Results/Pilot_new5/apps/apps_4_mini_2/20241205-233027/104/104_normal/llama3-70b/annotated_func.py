#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and a is a list of n integers where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if all(a[k] - a[i] == k - i for k in range(i, j)):
                max_erase = max(max_erase, j - i - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `max_erase` is the maximum number of consecutive elements that can be erased from the list `a` based on the conditions checked for all pairs of indices `(i, j)`, and `i` ranges from 0 to `n-1` indicating the start of the erasure check. If no elements can be erased, `max_erase` remains 0.
    print(max_erase)
#Overall this is what the function does:The function accepts an integer `n`, representing the number of elements, and a list `a` of `n` strictly increasing integers. It calculates the maximum number of consecutive elements that can be erased from the list based on a specific condition: for any subarray of `a` defined by indices `(i, j)`, it checks if the difference between elements is equal to their respective index differences. The function prints the maximum number of elements that can be erased, which could be less than or equal to `n-1`. If no elements can be erased based on the condition, it returns 0.

