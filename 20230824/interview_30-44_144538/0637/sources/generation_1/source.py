
n = int(input())
photo = list(map(int, input().split()))

# check if there is a valid pattern of alternating stripes
def check_photo(photo):
    num_stripes = 0
    current_stripe = None
    stripe_width = 0
    
    for pixel in photo:
        if current_stripe is None:
            current_stripe = pixel
            stripe_width += 1
        elif current_stripe == pixel:
            stripe_width += 1
        else:
            # check if previous stripe width is equal or -1 (not yet set)
            if stripe_width != -1 and num_stripes != 0 and stripe_width != num_stripes:
                return False
            else:
                num_stripes = stripe_width
                current_stripe = pixel
                stripe_width = 1
    
    # check if last stripe width is equal to the rest
    if stripe_width != -1 and stripe_width != num_stripes:
        return False
    
    return True

if check_photo(photo):
    print("YES")
else:
    print("NO")
    