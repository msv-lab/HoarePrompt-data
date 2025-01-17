# Read input values
A, B, C, N = map(int, input().split())

# Calculate the number of students who only visited BugDonalds and BeaverKing
only_bugdonalds = A - C
only_beaverking = B - C
both = C

# Check for invalid conditions
if only_bugdonalds < 0 or only_beaverking < 0 or both < 0:
    print(-1)
elif only_bugdonalds + only_beaverking + both >= N:
    print(-1)
else:
    # Calculate the number of students who didn't pass the exam
    failed_students = N - (only_bugdonalds + only_beaverking + both)
    if failed_students > 0:
        print(failed_students)
    else:
        print(-1)
