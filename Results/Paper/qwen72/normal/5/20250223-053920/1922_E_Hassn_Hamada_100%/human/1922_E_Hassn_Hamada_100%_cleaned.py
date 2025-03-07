stdin = sys.stdin
stdout = sys.stdout

def func_1(number: int, sequence: List[int]):
    """
    Generates a sequence of numbers based on the input number.
 
    Args:
        number (int): The input number to generate sequence for
        sequence (List[int]): The output sequence 
    """
    assert number >= 0
    if number == 0:
        return (0, 0)
    size_overlap = (0, 0)
    for i in range(max(sequence, default=0), -1, -1):
        (size, value) = (i + 1, (1 << i + 1) - (1 << i))
        while (1 << size + 1) - (1 << i) <= number:
            size += 1
            value = (1 << size) - (1 << i)
        if value <= number:
            size_overlap = (size, i)
            break
    (size, overlap) = size_overlap
    for i in range(size - overlap):
        sequence.append(i + overlap)
    func_1(number - (1 << size) + (1 << overlap), sequence)
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    result = list()
    func_1(n - 1, result)
    print(len(result))
    print(' '.join(map(str, result)))