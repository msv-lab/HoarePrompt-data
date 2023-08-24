w, h = map(int, input().split())

image = []
for _ in range(h):
    row = input()
    image.append(row)

# Rotate the image 90 degrees clockwise
rotated_image = []
for i in range(w-1, -1, -1):
    rotated_row = ''
    for j in range(h):
        rotated_row += image[j][i]
    rotated_image.append(rotated_row)

# Flip the image horizontally
flipped_image = []
for row in rotated_image[::-1]:
    flipped_image.append(row)

# Zoom in twice on the image
zoomed_image = []
for row in flipped_image:
    zoomed_row = ""
    for pixel in row:
        zoomed_row += pixel * 2
    zoomed_image.append(zoomed_row)
    zoomed_image.append(zoomed_row)

# Print the result
for row in zoomed_image:
    print(row)