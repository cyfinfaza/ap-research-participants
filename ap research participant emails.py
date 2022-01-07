import csv

parentalConsent = set()

with open(input("List of students with parental consent (csv): ")) as file:
    data = csv.reader(file)
    for row in data:
        parentalConsent.add(f"{row[1].lower()}{row[0].lower()}@bernardsboe.com")

studentAssent = set()

with open(input("List of students with student consent (csv): ")) as file:
    data = csv.reader(file)
    for row in data:
        studentAssent.add(f"{row[1].lower()}{row[0].lower()}@bernardsboe.com")
# print(studentAssent)

parentNoStudent = parentalConsent - studentAssent

print("\n".join(parentNoStudent))

with open(input("Save as: "), "w") as file:
    file.write("\n".join(parentNoStudent))
