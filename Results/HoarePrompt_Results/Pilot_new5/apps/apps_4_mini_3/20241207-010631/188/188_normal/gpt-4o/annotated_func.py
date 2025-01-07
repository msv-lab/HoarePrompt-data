#State of the program right berfore the function call: n is an even integer in the range [2, 100], and the subsequent n integers (a_1, a_2, ..., a_n) are in the range [1, 100].
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
        #State of the program after the if-else block has been executed: *`n` is an even integer in the range [2, 100]; `cards` is a list of `n` integers based on user input; `count` is a Counter object representing the frequency of each integer in `cards`; `unique_numbers` is a list of unique integers from `cards`, sorted by their frequency in ascending order; the length of `unique_numbers` is greater than or equal to 2. If the count of the most frequent integer and the second most frequent integer both equal `n // 2`, then 'YES' is printed along with the values of `unique_numbers[-1]` and `unique_numbers[-2]`. Otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`n` is an even integer in the range [2, 100]; `cards` is a list of `n` integers based on user input; `count` is a Counter object representing the frequency of each integer in `cards`; `unique_numbers` is a list of unique integers from `cards`, sorted by their frequency in ascending order. If the length of `unique_numbers` is less than 2, 'NO' has been printed. If the length of `unique_numbers` is greater than or equal to 2, then if the count of the most frequent integer and the second most frequent integer both equal `n // 2`, 'YES' is printed along with the values of `unique_numbers[-1]` and `unique_numbers[-2]`; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (in the range [2, 100]) and reads `n` integers from user input (each in the range [1, 100]). It counts the frequency of each integer and checks for two most frequent unique numbers. If there are fewer than two unique numbers, it prints 'NO'. If the two most frequent numbers each appear exactly `n // 2` times, it prints 'YES' along with those numbers; otherwise, it prints 'NO'. It does not handle cases where the input might be outside the expected ranges or where the input cannot be converted to integers.

