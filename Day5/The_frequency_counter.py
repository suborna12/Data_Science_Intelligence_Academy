st = "banana"
freq = {}
for char in st:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)