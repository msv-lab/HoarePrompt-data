def cal_sum(n):
    perrin_sequence = [3, 0, 2]
    for i in range(3, n):
        perrin_sequence.append(perrin_sequence[i-2] + perrin_sequence[i-3])
    return sum(perrin_sequence[:n])
