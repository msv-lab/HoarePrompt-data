#State of the program right berfore the function call: n is an even integer between 2 and 100, and there are n integers (1 ≤ a_i ≤ 100) representing numbers written on the n cards.
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
        #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100. If the counts of `unique_numbers[-1]` and `unique_numbers[-2]` are both equal to `n // 2`, 'YES' is printed along with the values of `unique_numbers[-1]` and `unique_numbers[-2]`. Otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100; `cards` is a list of `n` integers from user input; `count` is a Counter object representing counts of integers in `cards`; `unique_numbers` is a sorted list of keys from `count`. If `unique_numbers` has less than 2 elements, 'NO' is printed. Otherwise, if the counts of `unique_numbers[-1]` and `unique_numbers[-2]` are both equal to `n // 2`, 'YES' is printed along with the values of `unique_numbers[-1]` and `unique_numbers[-2]`. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function reads an even integer `n` (between 2 and 100) and `n` integers from user input, representing the values on cards. It counts the occurrences of each integer using a Counter and creates a sorted list of unique integers based on their counts. If there are fewer than 2 unique integers, it outputs 'NO'. If there are at least 2 unique integers, it checks if the two most frequently occurring integers both appear exactly `n // 2` times. If they do, it outputs 'YES' along with these two integers; otherwise, it outputs 'NO'. If all conditions are followed, it does not return any value but rather prints the results based on the derived conditions. Missing functionality includes the absence of error handling for invalid inputs such as non-integer values or integers outside the specified range.

