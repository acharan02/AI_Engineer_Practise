student_name = input("Enter the student's name: ")
marks = []
for i in range(5):
    mark = int(input(f"Enter the mark for subject {i + 1}: "))
    while mark < 0 or mark > 100:
        print("Invalid mark. Please enter a mark between 0 and 100.")
        mark = int(input(f"Enter the mark for subject {i + 1}: "))

    marks.append(mark)
print(f"Marks for {student_name}: {marks}")
total = 0
for mark in marks:
    total = total + mark 
average_marks = total / len(marks)
print (f"Total marks: {total}")
print(f"Average marks: {average_marks:.2f}")
failed = False

for mark in marks:
    if mark < 35:
        failed = True
        break

if failed:
    print(f"{student_name} has failed.")

elif average_marks >= 90:
    print(f"{student_name} has achieved Grade A.")

elif average_marks >= 80:
    print(f"{student_name} has achieved Grade B.")

elif average_marks >= 70:
    print(f"{student_name} has achieved Grade C.")

elif average_marks >= 60:
    print(f"{student_name} has achieved Grade D.")

else:
    print(f"{student_name} has passed.")
print("\n" + "=" * 35)
print("       STUDENT RESULT REPORT")
print("=" * 35)

print(f"Student Name : {student_name}")
print(f"Subject Marks: {marks}")
print(f"Total Marks  : {total}/500")
print(f"Average      : {average_marks:.2f}%")

print("=" * 35)