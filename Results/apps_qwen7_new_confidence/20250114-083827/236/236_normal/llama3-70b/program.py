n = int(input())
k = 1
while True:
    candies = n
    vasya_eaten = 0
    while candies > 0:
        vasya_eaten += min(k, candies)
        candies -= min(k, candies)
        petya_eaten = candies // 10
        candies -= petya_eaten
    if vasya_eaten * 2 >= n:
        print(k)
        break
    k += 1
