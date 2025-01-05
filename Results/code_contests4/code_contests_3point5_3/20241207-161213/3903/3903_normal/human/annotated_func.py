#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100. The input sequence consists of n integers, each being either 0 or 1.**
def func():
    n = int(input())
    a = map(int, raw_input().split())
    maximum_count = 0
    for start in range(0, n):
        for end in range(0, n):
            if start <= end:
                b = list(a)
                for i in range(start, end + 1):
                    b[i] = 1 - b[i]
                count = sum(b)
                maximum_count = max(maximum_count, count)
        
    #State of the program after the  for loop has been executed: `a` is a list of integers where each integer is either 0 or 1, `maximum_count` is the maximum sum of 1s in list `a` after toggling elements, `n` is greater than 0, `start` is equal to `n-1`, `end` is equal to `n-1`, `b` is a copy of list `a` with all elements toggled, `count` is the sum of 1s in list `b`
    print(maximum_count)
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, representing the number of integers in the input sequence. The input sequence consists of `n` integers, each being either 0 or 1. The function then processes the input sequence by toggling elements and calculating the maximum sum of 1s in the list `a`. Finally, it prints out the maximum count of 1s after toggling elements. The function does not explicitly return a value.

