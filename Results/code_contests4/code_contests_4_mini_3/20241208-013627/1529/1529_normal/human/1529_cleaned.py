numbers = [int(x) for x in raw_input().split()]
numbers.sort()
print('{0} {1} {2}'.format(numbers[3] - numbers[0], numbers[3] - numbers[1], numbers[3] - numbers[2]))