#State of the program right berfore the function call: The input consists of an even number of integers (n), followed by n integers representing the numbers written on the cards, such that 2 ≤ n ≤ 100 and 1 ≤ a_i ≤ 100 for all i.
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
        #State of the program after the if-else block has been executed: `n` is an even integer between 2 and 100 (inclusive), `cards` is a list of `n` input integers, `count` is a dictionary where keys are the unique integers from `cards` and values are their respective counts, `unique_numbers` is a list of unique integers from `cards` sorted by their counts, and the number of unique integers in `unique_numbers` is 2 or more. If `count[unique_numbers[-1]]` equals `n // 2` and `count[unique_numbers[-2]]` equals `n // 2`, then 'YES' has been printed to the console along with `unique_numbers[-1]` and `unique_numbers[-2]`. Otherwise, 'NO' has been printed to the console.
    #State of the program after the if-else block has been executed: *`n` is an even integer between 2 and 100 (inclusive), `cards` is a list of `n` input integers, `count` is a dictionary where keys are the unique integers from `cards` and values are their respective counts, `unique_numbers` is a list of unique integers from `cards` sorted by their counts. If `unique_numbers` has less than 2 unique integers, the string 'NO' has been printed. If `unique_numbers` has 2 or more unique integers, then if `count[unique_numbers[-1]]` equals `n // 2` and `count[unique_numbers[-2]]` equals `n // 2`, 'YES' has been printed to the console along with `unique_numbers[-1]` and `unique_numbers[-2]`, otherwise 'NO' has been printed to the console.
#Overall this is what the function does:The function reads an even number of integers, counts the occurrences of each, and checks if the counts of the two most frequent numbers are equal to half the total count. If so, it prints 'YES' with these numbers; otherwise, it prints 'NO', handling cases implicitly based on the counts and total number of cards.

