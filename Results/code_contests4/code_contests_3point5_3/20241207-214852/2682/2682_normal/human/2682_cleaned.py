for line in stdin:
    (number, weight, height) = line.split(',')
    if 25.0 <= float(weight) / float(height) ** 2:
        print(number)