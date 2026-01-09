def running_average():
    total = 0
    count = 0
    while True:
        value = yield total / count if count > 0 else 0
        total += value
        count += 1

running_avg = running_average()
next(running_avg)
print("Input a sequence of numbers (Press Enter & 'e' to quit):")
while True:
    num = input("> ")
    if num.lower() == 'e':
        break
    value = float(num)
    average = running_avg.send(value)
    print("Running Average:", average)
