#State of the program right berfore the function call: n is an even integer between 2 and 100, and a list of n integers where each integer is between 1 and 100 represents the numbers on the cards.
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
        #State of the program after the if-else block has been executed: *`n` is an integer; `cards` is a list of `n` integers where each integer is between 1 and 100; `count` is a Counter object containing counts of each integer in `cards`; `unique_numbers` is a sorted list of the keys of `count`, sorted by their counts in ascending order. If `count[unique_numbers[-1]]` and `count[unique_numbers[-2]]` are both equal to `n // 2`, the output 'YES' is printed along with the values `unique_numbers[-1]` and `unique_numbers[-2]`. Otherwise, the output is 'NO'.
    #State of the program after the if-else block has been executed: *`n` is an integer; `cards` is a list of `n` integers where each integer is between 1 and 100; `count` is a Counter object containing counts of each integer in `cards`; `unique_numbers` is a sorted list of the keys of `count`, sorted by their counts in ascending order. If the length of `unique_numbers` is less than 2, the output is 'NO'. Otherwise, if the counts of the two most frequent unique numbers are both equal to `n // 2`, the output is 'YES' along with the values `unique_numbers[-1]` and `unique_numbers[-2]`; otherwise, the output is 'NO'.
#Overall this is what the function does:The function accepts an even integer `n` (between 2 and 100) and a list of `n` integers (each between 1 and 100). It checks if there are at least two unique numbers in the list. If there are, it then checks if the two most frequent unique numbers both appear exactly `n // 2` times. If both conditions are satisfied, it prints 'YES' along with these two numbers; otherwise, it prints 'NO'. If there are fewer than two unique numbers, it also prints 'NO'. The function does not handle cases where the input is invalid (e.g., if `n` is not even or not within the specified range).

