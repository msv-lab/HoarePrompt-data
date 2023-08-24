def count_passwords(password):
    count = 1
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(password)):
        # If a consonant is found
        if password[i] not in vowels:
            # If the previous character is a consonant or i = 0, we can double the count
            if i == 0 or password[i-1] not in vowels:
                count = (count * 2) % 1000009

    return count

password = input()
print(count_passwords(password))