#State of the program right berfore the function call: n is an even integer between 2 and 100, and the subsequent n integers are between 1 and 100, representing the numbers written on the n cards.
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
        #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100; `cards` is a list of `n` integers obtained from input; `count` is a Counter object representing the occurrences of each integer in `cards`; `unique_numbers` is a list of unique integers from `cards` sorted by their occurrences in ascending order, with a length of 2 or more. If both the counts of the last and second to last unique numbers in `unique_numbers` are equal to `n // 2`, then 'YES' is printed, followed by the last unique number and the second to last unique number from `unique_numbers`. Otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100; `cards` is a list of `n` integers obtained from input; `count` is a Counter object representing the occurrences of each integer in `cards`; and `unique_numbers` is a list of unique integers from `cards` sorted by their occurrences in ascending order. If the length of `unique_numbers` is less than 2, 'NO' is printed. Otherwise, if the length of `unique_numbers` is 2 or more, and the counts of the last and second to last unique numbers in `unique_numbers` are both equal to `n // 2`, then 'YES' is printed along with the last and second to last unique numbers; if not, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (with a value between 2 and 100) representing the number of cards, followed by `n` integers (each between 1 and 100) that represent the values on those cards. It checks if there are at least two unique card values and counts their occurrences using a Counter. If the last two unique numbers have the same count equal to `n // 2`, it prints 'YES' along with those two numbers. If there are fewer than two unique numbers or the conditions on the counts are not met, it prints 'NO'.

