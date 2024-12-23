def func_1(tuples):
    num_elements = len(tuples[0])
    averages = []
    for i in range(num_elements):
        elements_at_position = [t[i] for t in tuples]
        avg = sum(elements_at_position) / len(tuples)
        averages.append(avg)
    return averages
assert func_1(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))) == [30.5, 34.25, 27.0, 23.25]
assert func_1(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))) == [25.5, -18.0, 3.75]
assert func_1(((100, 100, 100, 120), (300, 450, 560, 450), (810, 800, 390, 320), (10, 20, 30, 40))) == [305.0, 342.5, 270.0, 232.5]