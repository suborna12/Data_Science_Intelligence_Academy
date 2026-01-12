data = ["100px", "20px", "3px"]
srt = sorted(data, key=lambda x: int(x[:-2]))
print(srt)