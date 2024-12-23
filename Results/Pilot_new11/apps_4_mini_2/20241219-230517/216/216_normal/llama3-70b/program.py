n = int(input())
s = input()
lowercase = [i for i, c in enumerate(s) if c.islower()]
print(len(lowercase))
