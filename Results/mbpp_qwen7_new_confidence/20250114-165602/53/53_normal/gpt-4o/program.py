def next_smallest_palindrome(num: int) -> int:
    def is_palindrome(n: int) -> bool:
        return str(n) == str(n)[::-1]
    
    num += 1  # Start checking from the next number
    while not is_palindrome(num):
        num += 1
    return num

# Test cases
assert next_smallest_palindrome(99) == 101
assert next_smallest_palindrome(1221) == 1331
assert next_smallest_palindrome(120) == 121
