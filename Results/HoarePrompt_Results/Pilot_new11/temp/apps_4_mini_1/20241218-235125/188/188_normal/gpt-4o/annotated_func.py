#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 100, and the following n integers a_i (where 1 ≤ a_i ≤ 100) represent the numbers written on the n cards.
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
        #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ n ≤ 100; `cards` is a list of `n` integers obtained from input, where each integer is within the range of 1 to 100; `count` is a Counter object representing the frequencies of each integer in `cards`; `unique_numbers` is a sorted list of unique integers based on their frequency in ascending order and has a length of 2 or greater. If the count of the most frequent integer and the second most frequent integer in `unique_numbers` are both equal to n // 2, then the output is 'YES' and the printed values are the two most frequent integers in `unique_numbers`. Otherwise, the output is 'NO'.
    #State of the program after the if-else block has been executed: *`n` is an even integer such that 2 ≤ `n` ≤ 100; `cards` is a list of `n` integers obtained from input, where each integer is within the range of 1 to 100; `count` is a Counter object representing the frequencies of each integer in `cards`; `unique_numbers` is a sorted list of unique integers based on their frequency in ascending order. If the length of `unique_numbers` is less than 2, the output is 'NO'. Otherwise, if `unique_numbers` has a length of 2 or greater, the output is 'YES' if the most frequent and the second most frequent integers in `unique_numbers` both have a frequency of n // 2, with the printed values being these two most frequent integers; otherwise, the output is 'NO'.
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 100) and reads `n` integers, each within the range of 1 to 100, from standard input. It counts the frequency of each integer and sorts the unique integers by their frequency. If there are fewer than two unique integers, it prints 'NO'. If there are at least two unique integers, it checks if both the most frequent and the second most frequent integers each appear exactly `n//2` times. If this condition is met, it prints 'YES' followed by the two integers; otherwise, it prints 'NO'. In summary, the function determines if the integers can be evenly divided into two groups of equal size consisting of the two most frequent integers. If the conditions for these groups are not met or unique integers are insufficient, no successful grouping is reported.

