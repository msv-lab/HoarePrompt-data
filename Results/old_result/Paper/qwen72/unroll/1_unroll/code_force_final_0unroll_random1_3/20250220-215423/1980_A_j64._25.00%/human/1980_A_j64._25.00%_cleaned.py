def func_1(t, test_cases):
    """
    Calculate the minimum number of problems Vlad needs to create.
 
    Args:
        t (int): Number of test cases.
        test_cases (list): List of test cases, where each test case is a tuple containing
            - n (int): Number of problems in the bank.
            - m (int): Number of upcoming rounds.
            - a (str): String of problem difficulties.
 
    Returns:
        list: List of results, one for each test case.
    """
    results = []
    for _ in range(t):
        (n, m, a) = test_cases[_]
        freq = [0] * 7
        for prob in a:
            freq[ord(prob) - ord('A')] += 1
        missing = sum((max(0, m - f) for f in freq))
        results.append(missing)
    return results
t = 3
test_cases = [(10, 1, 'BGECDCBDED'), (10, 2, 'BGECDCBDED'), (9, 1, 'BBCDEFFGG')]
results = func_1(t, test_cases)
for result in results:
    print(result)