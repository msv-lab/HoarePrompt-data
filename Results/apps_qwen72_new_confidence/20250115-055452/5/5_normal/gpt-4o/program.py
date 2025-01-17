def contains_seven(h, m):
    """Check if the time h:m contains a '7'."""
    return '7' in str(h) or '7' in str(m)

def main():
    # Read inputs
    x = int(input())
    hh, mm = map(int, input().split())

    # Initialize the counter for the number of snooze presses
    snooze_count = 0

    # Check the time and keep pressing snooze until a lucky time is found
    while not contains_seven(hh, mm):
        snooze_count += 1
        mm -= x
        if mm < 0:
            mm += 60
            hh -= 1
            if hh < 0:
                hh += 24

    # Print the result
    print(snooze_count)

# Run the main function
if __name__ == "__main__":
    main()
