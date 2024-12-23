#State of the program right berfore the function call: n is an even integer between 2 and 100 inclusive, and the list of cards contains n integers, where each integer is between 1 and 100 inclusive.
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
        #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100 inclusive; `cards` is a list containing `n` integers each between 1 and 100 inclusive; `count` is a Counter object representing the frequency distribution of `cards`; `unique_numbers` is a sorted list of unique keys from `count` based on their frequency with a length of 2 or more. If the last two unique numbers in `unique_numbers` each appear exactly `n // 2` times, these numbers are printed. Otherwise, the printed output is 'NO'.
    #State of the program after the if-else block has been executed: *`n` is an input even integer between 2 and 100 inclusive; `cards` is a list containing `n` integers each between 1 and 100 inclusive; `count` is a Counter object representing the frequency distribution of `cards`; `unique_numbers` is a sorted list of unique keys from `count` based on their frequency. If `unique_numbers` contains less than 2 unique elements, the output is 'NO'. If `unique_numbers` has a length of 2 or more and the last two unique numbers each appear exactly `n // 2` times, those numbers are printed. Otherwise, the printed output is 'NO'.
#Overall this is what the function does:The function reads an even integer `n` (between 2 and 100 inclusive) from input, followed by `n` integers representing cards (each between 1 and 100 inclusive). It counts the frequency of each unique card and sorts them by their frequency. If there are fewer than two unique card values, it outputs 'NO'. If there are at least two unique card values, it checks if the two most frequent cards both appear exactly `n // 2` times. If so, it prints 'YES' followed by the two card values; otherwise, it prints 'NO'. In cases where the input does not follow the expected format (non-integer values, odd `n`, etc.), the function lacks error handling and will cause a runtime error instead of gracefully managing those scenarios.

