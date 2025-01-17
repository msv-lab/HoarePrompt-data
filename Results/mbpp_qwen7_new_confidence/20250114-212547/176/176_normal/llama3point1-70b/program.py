def overlapping(seq1, seq2):
    return any(element in seq2 for element in seq1)
