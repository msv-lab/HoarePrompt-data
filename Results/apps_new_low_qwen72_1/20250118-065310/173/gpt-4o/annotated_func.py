#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, a and b are lists of integers of length n, and each element in a and b is an integer between 1 and 5 inclusive.
def func():
    n = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

count_a = [0] * 6

count_b = [0] * 6
    for performance in a:
        count_a[performance] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 100\), `a` is a list of integers of length `n` where each element is between 1 and 5 inclusive, `b` is a list of integers of length `n` where each element is between 1 and 5 inclusive, `count_a` is a list of integers of length 6 where each element at index `i` represents the count of occurrences of `i` in `a`, `count_b` is `[0, 0, 0, 0, 0, 0]`. The loop executes exactly `n` times, incrementing the corresponding index in `count_a` based on the value of each element in `a`. If `n` is 0, the loop does not execute, and `count_a` remains `[0, 0, 0, 0, 0, 0]`.
    for performance in b:
        count_b[performance] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 100\), `a` is a list of integers of length `n` where each element is between 1 and 5 inclusive, `b` is a list of integers of length `n` where each element is between 1 and 5 inclusive, `count_a` is a list of integers of length 6 where each element at index `i` represents the count of occurrences of `i` in `a`, `count_b` is a list of integers of length 6 where each element at index `i` represents the count of occurrences of `i` in `b`.
    for i in range(1, 6):
        if (count_a[i] + count_b[i]) % 2 != 0:
            print(-1)
            exit()
        
    #State of the program after the  for loop has been executed: `i` is 6, `n` is an integer such that \(1 \leq n \leq 100\), `a` is a list of integers of length `n` where each element is between 1 and 5 inclusive, `b` is a list of integers of length `n` where each element is between 1 and 5 inclusive, `count_a` is a list of integers of length 6 where each element at index `i` represents the count of occurrences of `i` in `a`, `count_b` is a list of integers of length 6 where each element at index `i` represents the count of occurrences of `i` in `b`. The loop has completed all 5 iterations. If any of the sums \((count_a[i] + count_b[i]) \% 2\) for \(i\) in [1, 5] is odd, the program has printed -1 and exited. If none of these sums are odd, the program continues without any changes to the variables.
    exchanges_needed = 0
    for i in range(1, 6):
        diff = abs(count_a[i] - count_b[i]) // 2
        
        exchanges_needed += diff
        
    #State of the program after the  for loop has been executed: i is 6, n is an integer such that \(1 \leq n \leq 100\), a is a list of integers of length n where each element is between 1 and 5 inclusive, b is a list of integers of length n where each element is between 1 and 5 inclusive, count_a is a list of integers of length 6 where each element at index i represents the count of occurrences of i in a, count_b is a list of integers of length 6 where each element at index i represents the count of occurrences of i in b, exchanges_needed is the sum of (abs(count_a[j] - count_b[j]) // 2) for j in [1, 2, 3, 4, 5], provided that (count_a[i] + count_b[i]) % 2 == 0 for all i in [1, 5]; otherwise, the program prints -1 and exits.
    print(exchanges_needed // 2)
#Overall this is what the function does:The function reads an integer `n` and two lists `a` and `b` of integers from the user. Each list `a` and `b` contains `n` integers, and each integer is between 1 and 5 inclusive. The function then counts the occurrences of each integer (from 1 to 5) in both lists `a` and `b`. It checks if the total count of each integer across both lists is even. If any of these totals is odd, the function prints `-1` and exits. If all totals are even, the function calculates the minimum number of swaps required to make the counts of each integer in `a` and `b` equal and prints this number. The function does not return any value; it only prints the result. Potential edge cases include when `n` is 0 (which would result in empty lists, but this case is not handled in the code).

