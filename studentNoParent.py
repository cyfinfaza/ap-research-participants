import csv

names = {}

parentalConsent = set()

with open(input("List of students with parental consent (csv): ")) as file:
    data = csv.reader(file)
    for row in data:
        email = f"{row[1].lower()}{row[0].lower()}@bernardsboe.com"
        parentalConsent.add(email)
        names[email] = f"{row[3]} {row[1]} {row[0]}"

studentAssent = set()

with open(input("List of students with student consent (csv): ")) as file:
    data = csv.reader(file)
    for row in data:
        email = f"{row[1].lower()}{row[0].lower()}@bernardsboe.com"
        studentAssent.add(email)
        names[email] = f"{row[3]} {row[1]} {row[0]}"
# print(studentAssent)

studentNoParent = studentAssent - parentalConsent

for student in studentNoParent:
    print(names[student])

print("\n".join(studentNoParent))

with open(input("Save as: "), "w") as file:
    file.write("\n".join(studentNoParent))
