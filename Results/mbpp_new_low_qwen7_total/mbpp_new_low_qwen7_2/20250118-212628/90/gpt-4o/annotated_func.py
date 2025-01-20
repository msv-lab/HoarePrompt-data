#State of the program right berfore the function call: lst is a list of integers.
def func_1(lst):
    even_count = sum(1 for x in lst if x % 2 == 0)

odd_count = len(lst) - even_count

even_pairs = even_count * (even_count - 1) // 2

odd_pairs = odd_count * (odd_count - 1) // 2
    return even_pairs + odd_pairs
    #`The program returns the sum of the number of unique even pairs (even_pairs) and the number of unique odd pairs (odd_pairs)`
#Overall this is what the function does:The function `func_1` accepts a list of integers `lst` and calculates the sum of the number of unique pairs where both elements are even (`even_pairs`) and the number of unique pairs where both elements are odd (`odd_pairs`). It returns this total sum. The function first counts the number of even and odd numbers in the list, then uses these counts to determine the possible unique pairs of even and odd numbers. Any potential edge cases, such as an empty list or a list with only even or odd numbers, are handled correctly.

