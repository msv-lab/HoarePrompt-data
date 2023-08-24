n = int(input())
photo = list(map(int, input().split()))

def check_photo(photo):
    num_stripes = 0
    current_stripe = None
    stripe_width = -1
    
    for pixel in photo:
        if current_stripe is None:
            current_stripe = pixel
            stripe_width = 1
        elif current_stripe == pixel:
            stripe_width += 1
        else:
            if stripe_width != -1 and stripe_width != num_stripes:
                return False
            else:
                num_stripes = stripe_width
                current_stripe = pixel
                stripe_width = 1
    
    if stripe_width != -1 and stripe_width != num_stripes:
        return False
    
    return True

if check_photo(photo):
    print("YES")
else:
    print("NO")