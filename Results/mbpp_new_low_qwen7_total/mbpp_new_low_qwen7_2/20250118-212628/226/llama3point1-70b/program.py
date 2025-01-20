def find_Odd_Pair(arr, n):
    odd_count = sum(1 for num in arr if num % 2 != 0)
    even_count = n - odd_count
    return odd_count * even_count + (odd_count * (odd_count - 1)) // 2
