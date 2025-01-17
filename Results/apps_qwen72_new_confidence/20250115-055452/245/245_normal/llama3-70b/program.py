n = int(input())
x = int(input())

initial_position = (x - (n % 2)) % 3
print(initial_position)
