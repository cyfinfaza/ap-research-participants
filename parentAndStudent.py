import csv

parentalConsent = set()

with open(input("List of students with parental consent (csv): ")) as file:
    data = csv.reader(file)
    for row in list(data)[1:]:
        parentalConsent.add(f"{row[3]}	{row[0]}	{row[1]}	{row[2]}")

studentAssent = set()

with open(input("List of students with student consent (csv): ")) as file:
    data = csv.reader(file)
    for row in list(data)[1:]:
        studentAssent.add(f"{row[3]}	{row[0]}	{row[1]}	{row[2]}")

parentAndStudent = parentalConsent.intersection(studentAssent)

print("Students with parental and student consent:")
for student in parentAndStudent:
    print(student)

print("Emails")
emails = []
for student in parentAndStudent:
    emails.append(
        student.split("	")[2].lower()
        + student.split("	")[1].lower()
        + "@bernardsboe.com"
    )
print("\n".join(emails))

with open(input("Save as: "), "w") as file:
    file.write("\n".join(emails))
