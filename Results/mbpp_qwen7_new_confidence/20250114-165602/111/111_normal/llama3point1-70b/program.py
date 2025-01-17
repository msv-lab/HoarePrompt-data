def next_Perfect_Square(n: int) -> int:
    i = 1
    while True:
        perfect_square = i * i
        if perfect_square > n:
            return perfect_square
        i += 1
