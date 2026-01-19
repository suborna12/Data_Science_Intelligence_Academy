with open("big_file.txt", "w", encoding="utf-8") as f:
    for i in range (1000):
        f.write(f"{i}\n")