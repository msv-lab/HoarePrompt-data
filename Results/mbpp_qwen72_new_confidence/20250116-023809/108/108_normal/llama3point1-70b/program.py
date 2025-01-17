def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    else:
        total = 0
        for i in range(1, m + 1):
            total += get_total_number_of_sequences(m // i, n - 1)
        return total