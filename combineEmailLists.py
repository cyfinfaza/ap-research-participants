with open(input("List 1: ")) as file:
    lines = set([line.strip() for line in file.readlines()])

with open(input("List 2: ")) as file:
    lines2 = set([line.strip() for line in file.readlines()])

for line in lines2:
    lines.add(line)

print("\n".join(lines))

with open(input("Save as: "), "w") as file:
    file.write("\n".join(lines))
