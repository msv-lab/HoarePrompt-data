#State of the program right berfore the function call: n is an even number of integers (2 ≤ n ≤ 100), and each of the n lines contains a single integer (1 ≤ a_{i} ≤ 100) representing the number written on each card.
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
        #State of the program after the if-else block has been executed: *`n` is an integer input, `cards` is a list of `n` integers, `count` is a Counter object with elements from `cards` and their counts, `unique_numbers` is a list of unique numbers from `cards` sorted by their counts in ascending order. The length of `unique_numbers` is at least 2. If the last two elements of `unique_numbers` each occur exactly `n // 2` times, the last two elements of `unique_numbers` are printed. Otherwise, nothing specific is done (the program continues execution in a default state).
    #State of the program after the if-else block has been executed: *`n` is an integer input, `cards` is a list of `n` integers, `count` is a Counter object with elements from `cards` and their counts, `unique_numbers` is a list of unique numbers from `cards` sorted by their counts in ascending order. If the length of `unique_numbers` is less than 2, 'NO' is printed to the console. Otherwise, if the last two elements of `unique_numbers` each occur exactly `n // 2` times, these two elements are printed. Otherwise, no specific action is taken (the program continues execution in a default state).
#Overall this is what the function does:The function processes an even number of integers (2 ≤ n ≤ 100), where each integer (a_{i}) is between 1 and 100. It then counts the occurrences of each unique integer, sorts them by their counts, and checks if the two most frequent integers each occur exactly n // 2 times. If they do, it prints 'YES' followed by these two integers. If not, it prints 'NO'. If there are fewer than two unique numbers, it also prints 'NO'.

