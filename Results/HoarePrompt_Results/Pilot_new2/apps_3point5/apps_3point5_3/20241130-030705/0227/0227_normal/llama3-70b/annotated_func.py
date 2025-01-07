#State of the program right berfore the function call: 
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(1, n):
        if a[i] != a[i - 1] * 2:
            m += 1
        
    #State of the program after the  for loop has been executed: `n` must be greater than 1, `a` is a sorted list of integers, `m` is the number of times the condition `a[i] != a[i - 1] * 2` is true for all valid `i`, `i` is `n - 1`. If the condition is never true, `m` remains 1.
    print(m if m <= 23 else -1)
#Overall this is what the function does:The function reads an integer `n` as input, followed by a list of integers. It then sorts the list and iterates over the elements, counting the number of times an element is not twice the previous element. The function prints the count `m` if it is less than or equal to 23; otherwise, it prints -1. The function does not accept any parameters and provides specific output based on the sorted list of integers.

