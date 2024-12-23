#State of the program right berfore the function call: n is an even integer, and a list of integers `cards` of length n where each element represents the number written on a card (1 ≤ a_i ≤ 100).
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
        #State of the program after the if-else block has been executed: *`n` is an even integer, `cards` is a list of `n` integers, each between 1 and 100 inclusive, `count` is a dictionary-like object counting the occurrences of each element in `cards`, `unique_numbers` is a list of the unique numbers from `cards`, sorted based on their counts in ascending order, and the length of `unique_numbers` is at least 2. If the last two elements of `unique_numbers` are the same and their count is `n // 2`, the program prints these two elements. Otherwise, the program prints 'NO'.
    #State of the program after the if-else block has been executed: *`n` is an even integer, `cards` is a list of `n` integers (each between 1 and 100 inclusive), `count` is a dictionary-like object counting the occurrences of each element in `cards`, and `unique_numbers` is a list of the unique numbers from `cards`, sorted based on their counts in ascending order. If the length of `unique_numbers` is less than 2, the program prints 'NO'. Otherwise, if the last two elements of `unique_numbers` are the same and their count is `n // 2`, the program prints these two elements. Otherwise, the program prints 'NO'.
#Overall this is what the function does:The function takes a list of integers `cards` as input, where the length of the list is an even integer `n` and each element in the list is an integer between 1 and 100 inclusive. It then calculates the frequency of each unique number in the list using a counter. After sorting the unique numbers based on their frequencies in ascending order, the function checks if the last two elements in the sorted list have the same frequency and if this frequency is exactly half the length of the list (`n // 2`). If both conditions are met, it prints these two numbers and 'YES'. If either condition fails, it prints 'NO'. The function handles the following edge cases:
1. If the list has fewer than 2 unique numbers, it immediately prints 'NO'.
2. If the length of the list is not even, it would raise an error due to the initial input of `n` being read as an integer from the input, but this is not explicitly checked in the function.
3. If any number in the list is outside the range 1 to 100, it would raise an error when reading the input, but this is also not explicitly checked in the function.

