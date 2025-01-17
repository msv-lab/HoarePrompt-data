def even_position(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2))
