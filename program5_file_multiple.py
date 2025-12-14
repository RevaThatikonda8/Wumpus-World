with open("multi.txt", "w") as f:
    f.write("1\n2\n3\n4")

total = 0
with open("multi.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print("Total =", total)
