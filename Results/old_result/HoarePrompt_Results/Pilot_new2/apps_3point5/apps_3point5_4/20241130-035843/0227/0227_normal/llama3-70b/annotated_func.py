#State of the program right berfore the function call: n is a positive integer. All numbers in the sequence a are distinct positive integers.**
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(1, n):
        if a[i] != a[i - 1] * 2:
            m += 1
        
    #State of the program after the  for loop has been executed: `n` is greater than 1, `m` is the number of times `a[i]` is not equal to `a[i - 1] * 2` in the loop. If `a[i]` is equal to `a[i - 1] * 2` for all `i`, then `m` is 1.
    print(m if m <= 23 else -1)
#Overall this is what the function does:The function accepts a positive integer `n` and a sequence of distinct positive integers. It sorts the sequence and then iterates through the sorted array to find how many times an element is not twice the previous element. The function then prints the count of such occurrences, unless it exceeds 23, in which case it prints -1. Essentially, the function determines the maximum number of elements in the sequence that do not follow the pattern of being twice the previous element.

