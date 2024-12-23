#State of the program right berfore the function call: n is an even integer between 2 and 100 (inclusive), and a list of n integers, where each integer is between 1 and 100 (inclusive).
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
        #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 100, `cards` is a list of `n` integers, each between 1 and 100 (inclusive), `count` is a Counter object where each key is an integer from the list `cards` and its value is the count of that integer in the list `cards`, `unique_numbers` is a list of the unique numbers from `cards`, sorted by their frequency in descending order, and the length of `unique_numbers` is at least 2. If the last two elements in `unique_numbers` are present exactly `n // 2` times each in `cards`, the string 'YES' is printed to the console and the last two elements of `unique_numbers` are printed. Otherwise, the string 'NO' is printed to the console.
    #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 100, `cards` is a list of `n` integers, each between 1 and 100 (inclusive), `count` is a Counter object where each key is an integer from the list `cards` and its value is the count of that integer in the list `cards`, `unique_numbers` is a list of the unique numbers from `cards`, sorted by their frequency in descending order, and the string 'NO' is printed to the console unless the length of `unique_numbers` is at least 2 and the last two elements in `unique_numbers` are present exactly `n // 2` times each in `cards`, in which case the string 'YES' is printed followed by the last two elements of `unique_numbers`.
#Overall this is what the function does:The function accepts an even integer `n` between 2 and 100 (inclusive) and a list of `n` integers, each between 1 and 100 (inclusive). It counts the frequency of each integer in the list, sorts the unique integers by their frequency in descending order, and checks if there are at least two unique integers that appear exactly `n // 2` times each. If such integers exist, it prints 'YES' followed by these two integers; otherwise, it prints 'NO'. The function does not return any value. Potential edge cases include scenarios where `n` is 2, resulting in only two integers being provided, and situations where no two integers meet the condition of appearing exactly `n // 2` times.

