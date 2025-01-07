def func_1(radius, height):
    return 1 / 3 * math.pi * radius ** 2 * height
assert math.isclose(func_1(5, 12), 314.15926535897927, rel_tol=0.001)
assert math.isclose(func_1(10, 15), 1570.7963267948965, rel_tol=0.001)
assert math.isclose(func_1(19, 17), 6426.651371693521, rel_tol=0.001)