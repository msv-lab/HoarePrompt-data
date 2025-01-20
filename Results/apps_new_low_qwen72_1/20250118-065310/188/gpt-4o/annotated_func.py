#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 100, and a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 100 for each i.
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
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 100, `cards` is a list of `n` integers where each integer is between 1 and 100, `count` is a Counter object containing the frequency of each number in `cards`, `unique_numbers` is a list of the unique numbers in `cards` sorted by their frequency, and the length of `unique_numbers` is greater than or equal to 2. If the frequency of the most frequent number (`unique_numbers[-1]`) is `n // 2` and the frequency of the second most frequent number (`unique_numbers[-2]`) is also `n // 2`, the output of the code is 'YES' followed by the values of `unique_numbers[-1]` and `unique_numbers[-2]`. Otherwise, 'NO' has been printed.
    #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 100, `cards` is a list of `n` integers where each integer is between 1 and 100, `count` is a Counter object containing the frequency of each number in `cards`, and `unique_numbers` is a list of the unique numbers in `cards` sorted by their frequency. If the length of `unique_numbers` is less than 2, the state remains unchanged. If the length of `unique_numbers` is greater than or equal to 2, and the frequency of the most frequent number (`unique_numbers[-1]`) is `n // 2` and the frequency of the second most frequent number (`unique_numbers[-2]`) is also `n // 2`, the output of the code is 'YES' followed by the values of `unique_numbers[-1]` and `unique_numbers[-2]`. Otherwise, 'NO' has been printed.
#Overall this is what the function does:The function reads an even integer `n` (where 2 ≤ n ≤ 100) and a list of `n` integers (each between 1 and 100). It then determines if there are exactly two unique numbers in the list, each appearing exactly `n // 2` times. If this condition is met, the function prints 'YES' followed by the two numbers. Otherwise, it prints 'NO'. The function does not return any value; it only prints the result. Potential edge cases include when the list contains fewer than two unique numbers or when the frequencies of the two most frequent numbers do not match the required condition.

