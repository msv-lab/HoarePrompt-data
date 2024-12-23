#State of the program right berfore the function call: The input is a sequence of n integers, where n is an even number between 2 and 100 (inclusive), and each integer is between 1 and 100 (inclusive).
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
        #State of the program after the if-else block has been executed: *`n` is an even number between 2 and 100 (inclusive), `cards` is a list of n integers between 1 and 100 (inclusive), `count` is a dictionary where the keys are the unique integers in `cards` and the values are their respective frequencies in `cards`, `unique_numbers` is a list of the unique integers in `cards` sorted by their frequencies in ascending order, and the number of unique integers in `cards` is 2 or more. If the frequency of the most frequent integer in `cards` is equal to `n // 2` and the frequency of the second most frequent integer in `cards` is also equal to `n // 2`, then 'YES' has been printed along with the most and second most frequent integers. Otherwise, 'NO' has been printed to the console.
    #State of the program after the if-else block has been executed: `n` is an even number between 2 and 100 (inclusive), `cards` is a list of `n` integers between 1 and 100 (inclusive), `count` is a dictionary where the keys are the unique integers in `cards` and the values are their respective frequencies in `cards`, `unique_numbers` is a list of the unique integers in `cards` sorted by their frequencies in ascending order. If the number of unique integers in `cards` is less than 2, 'NO' is printed to the console. If the number of unique integers in `cards` is 2 or more, then if the frequency of the most frequent integer in `cards` is equal to `n // 2` and the frequency of the second most frequent integer in `cards` is also equal to `n // 2`, 'YES' has been printed along with the most and second most frequent integers; otherwise, 'NO' has been printed to the console.
#Overall this is what the function does:The function determines if a given sequence of n integers can be divided into two groups of equal size, each containing the same integer. It accepts a sequence of n integers as input, where n is an even number between 2 and 100 (inclusive), and each integer is between 1 and 100 (inclusive). The function returns 'YES' if the input sequence can be divided into two groups of equal size with the same integer, and it prints the two integers that make up the groups. Otherwise, it returns 'NO'. The function performs the following actions: (1) reads the input sequence of n integers, (2) counts the frequency of each integer in the sequence, (3) sorts the unique integers in ascending order of their frequencies, and (4) checks if the frequency of the most frequent integer and the second most frequent integer is equal to n // 2. If the input sequence contains less than 2 unique integers, the function immediately returns 'NO'. After executing, the program has the following state: the input sequence has been processed, and either 'YES' with the two integers that make up the groups or 'NO' has been printed to the console, depending on whether the input sequence meets the specified condition.

