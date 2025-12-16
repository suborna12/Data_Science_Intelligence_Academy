total = int(input("Enter a number of seconds: "))
hours = total // 3600
rem = total % 3600
minutes = rem // 60
second = rem % 60
print(f"{hours}h ; {minutes}min ; {second}sec")