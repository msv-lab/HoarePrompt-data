s = input()

t = []
u = []
stack = []

# Fill the stack with characters from s
for char in s:
    stack.append(char)

# Use a list to keep track of the count of each character in the stack
from collections import Counter
count = Counter(stack)

while stack or t:
    # Move all the characters from stack to t that are smaller than or equal to the smallest remaining in stack
    while stack and (not t or stack[-1] <= min(count)):
        t.append(stack.pop())
        count[t[-1]] -= 1
        if count[t[-1]] == 0:
            del count[t[-1]]
    # Append the last character of t to u
    u.append(t.pop())

print("".join(u))
