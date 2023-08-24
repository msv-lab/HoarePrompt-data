t = int(input())

for _ in range(t):
    n = int(input())
    pins = []
    changes = 0
    
    for _ in range(n):
        pin = input()
        pins.append(pin)
    
    pin_counts = {}
    
    for pin in pins:
        if pin not in pin_counts:
            pin_counts[pin] = 1
        else:
            pin_counts[pin] += 1
            changes += 1
    
    print(changes)
    
    for pin in pins:
        if pin_counts[pin] > 1:
            for i in range(10):
                new_pin = pin[:3] + str(i)
                if new_pin not in pin_counts:
                    pin_counts[new_pin] = 1
                    pin_counts[pin] -= 1
                    pin = new_pin
                    break
        print(pin)