#State of the program right berfore the function call: n is an even integer between 2 and 100, and the next n lines contain integers a_i where 1 ≤ a_i ≤ 100.
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
        #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100; `cards` is a list of `n` input integers; `count` is a Counter object representing the frequency of each integer in `cards`; `unique_numbers` is a sorted list of the keys in `count` based on their frequency in `cards`, and the length of `unique_numbers` is 2 or more. If both the frequencies of `unique_numbers[-1]` and `unique_numbers[-2]` are equal to `n // 2`, the output is `unique_numbers[-1]` and `unique_numbers[-2]`. Otherwise, the output 'NO' is printed.
    #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100; `cards` is a list of `n` input integers; `count` is a Counter object representing the frequency of each integer in `cards`; `unique_numbers` is a sorted list of the keys in `count` based on their frequency in `cards`. If the length of `unique_numbers` is less than 2, 'NO' is printed. Otherwise, if the length of `unique_numbers` is 2 or more and both frequencies of `unique_numbers[-1]` and `unique_numbers[-2]` are equal to `n // 2`, the output is `unique_numbers[-1]` and `unique_numbers[-2]`. If not, 'NO' is printed.
#Overall this is what the function does:The function accepts an even integer `n` (between 2 and 100) and then reads `n` integers from input (each between 1 and 100). It counts the frequency of each integer. If there are fewer than 2 unique integers, it prints 'NO'. If there are at least 2 unique integers, it checks if the two most common integers both appear exactly `n // 2` times. If so, it prints 'YES' followed by those two integers; otherwise, it prints 'NO'. If there are no integers or improper input is provided, the behavior is not explicitly defined in the code.

