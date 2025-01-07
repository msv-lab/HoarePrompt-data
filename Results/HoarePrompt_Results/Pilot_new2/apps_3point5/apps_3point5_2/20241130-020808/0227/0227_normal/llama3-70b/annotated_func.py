#State of the program right berfore the function call: n is a positive integer and a_1, a_2, ..., a_{n} are distinct positive integers.**
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(1, n):
        if a[i] != a[i - 1] * 2:
            m += 1
        
    #State of the program after the  for loop has been executed: `n` is greater than 1, `a` is a list of integers obtained by splitting the input and sorted in ascending order, `m` is the number of times `a[i]` is not equal to `a[i - 1] * 2` as `i` iterated over the range 1 to `n`.
    print(m if m <= 23 else -1)
#Overall this is what the function does:The function `func` reads a positive integer `n` and a list of `n` distinct positive integers. It then sorts the list and iterates through it to count the number of times an element is not exactly double the previous element. The final count `m` is printed unless it exceeds 23, in which case -1 is printed. The function does not explicitly return a value but provides output based on the calculated count `m`.

