cnt1 = int(input())
cnt2 = int(input())
cnt3 = int(input())
cnt4 = int(input())

# To form a regular bracket sequence:
# 1. The total number of opening brackets must equal the total number of closing brackets.
# 2. At any point in the sequence, the number of closing brackets should not exceed the number of opening brackets.

# Total opening brackets = cnt1 + cnt2
# Total closing brackets = cnt3 + cnt4

# For the sequence to be regular:
# cnt1 + cnt2 must equal cnt3 + cnt4
# Also, we need cnt2 >= cnt3 to ensure that the closing brackets never exceed the opening brackets at any point

if cnt1 + cnt2 == cnt3 + cnt4 and cnt2 >= cnt3:
    print(1)
else:
    print(0)
