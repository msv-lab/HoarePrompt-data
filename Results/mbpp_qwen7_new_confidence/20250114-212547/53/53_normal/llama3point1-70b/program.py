def next_smallest_palindrome(n: int) -> int:
    def is_palindrome(num: int) -> bool:
        return str(num) == str(num)[::-1]

    n += 1
    while not is_palindrome(n):
        n += 1
    return n
