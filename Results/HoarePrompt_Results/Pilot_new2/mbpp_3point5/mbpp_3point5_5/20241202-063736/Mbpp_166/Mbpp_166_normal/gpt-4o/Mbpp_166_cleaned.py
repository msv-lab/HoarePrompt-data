def func_1(lst):
    even_count = sum((1 for x in lst if x % 2 == 0))
    odd_count = len(lst) - even_count
    even_pairs = even_count * (even_count - 1) // 2
    odd_pairs = odd_count * (odd_count - 1) // 2
    return even_pairs + odd_pairs
assert func_1([5, 4, 7, 2, 1]) == 4
assert func_1([7, 2, 8, 1, 0, 5, 11]) == 9
assert func_1([1, 2, 3]) == 1