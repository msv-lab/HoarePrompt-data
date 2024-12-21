#State of the program right berfore the function call: n is an even integer between 2 and 100, and the next n lines contain integers a_i such that 1 ≤ a_i ≤ 100.
def func():
    n = int(input())
    cards = [int(input()) for _ in range(n)]
    count = Counter(cards)
    unique_numbers = sorted(count.keys(), key=lambda x: count[x])
    if (len(unique_numbers) < 2) :
        print('NO')
    else :
        if (count[unique_numbers[-1]] == n // 2 and count[unique_numbers[-2]] == n // 2) :
            print('YES')
            print(unique_numbers[-1], unique_numbers[-2])
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`n` is an input even integer between 2 and 100; `cards` is a list of `n` integers from input; `count` is a Counter object representing the frequency of each integer in `cards`; `unique_numbers` is a sorted list of the unique integers from `count.keys()` based on their frequency in ascending order, and the length of `unique_numbers` is greater than or equal to 2. If the counts of the two least frequent integers in `unique_numbers` are both equal to `n // 2`, `print` outputs `unique_numbers[-1]` and `unique_numbers[-2]`. Otherwise, the output is 'NO'.
    #State of the program after the if-else block has been executed: *`n` is an input even integer between 2 and 100, `cards` is a list of `n` integers, `count` is a Counter object representing the frequency of each integer in `cards`, and `unique_numbers` is a sorted list of the unique integers from `count.keys()` based on their frequency in ascending order. If the length of `unique_numbers` is less than 2, 'NO' is printed. If the length of `unique_numbers` is greater than or equal to 2, and the counts of the two least frequent integers are both equal to `n // 2`, the output is `unique_numbers[-1]` and `unique_numbers[-2]`; otherwise, 'NO' is printed.
#Overall this is what the function does:The function processes an even integer `n` (between 2 and 100) input following `n` integers, where each integer is between 1 and 100. It checks the frequency of these integers. If there are fewer than two unique integers, it outputs 'NO'. If there are at least two unique integers and the counts of the two least frequent integers are both equal to `n // 2`, it outputs 'YES', followed by the two integers. If the conditions are not met, it outputs 'NO'. The function does not accept parameters and reads directly from standard input. It has no explicit return value but communicates results through printed output. Potential edge cases include scenarios where all integers are the same or there are multiple integers, but their counts do not meet the required conditions for a 'YES' response.

