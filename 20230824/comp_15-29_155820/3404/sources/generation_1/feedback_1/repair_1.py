N, X = map(int, input().split())
encrypted_text = input().strip()

# Step 1: Define the function f(x) = (33x + 1) mod 2^20
def f(x):
    return (33 * x + 1) % (2**20)

# Step 2: Create the X by X grid
grid = [[0] * X for _ in range(X)]
x = 0
y = 0
for row in range(X):
    for col in range(X):
        grid[row][col] = f(x)
        x = (x + 1) % (2**20)
    y += 1

# Step 3: Sum all the values in every column
column_sums = [sum(column) % (2**20) for column in zip(*grid)]

# Step 4: Convert column sums to base 10
base_10_cols = int(''.join(str(col) for col in column_sums))

# Step 5: Convert base 10 to base 27
base_27_pad = ''
while base_10_cols > 0:
    base_27_pad += str(base_10_cols % 27)
    base_10_cols //= 27
base_27_pad = base_27_pad[::-1]

# Step 6: Shift letters in the encrypted text using the pad
decrypted_text = ''
for i in range(N):
    encrypted_letter = ord(encrypted_text[i]) - ord('A')
    if encrypted_letter == 26:
        decrypted_text += ' '
    else:
        shift = int(base_27_pad[i])
        decrypted_letter = (encrypted_letter - shift) % 27
        decrypted_text += chr(decrypted_letter + ord('A'))

# Step 7: Output the decrypted message
print(decrypted_text)