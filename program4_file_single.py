with open("single.txt", "w") as f:
    f.write("100")

with open("single.txt", "r") as f:
    print("Value from file:", f.read())
