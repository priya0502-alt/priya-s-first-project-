import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: User Inputs
# -----------------------------

num_students = int(input("Enter number of students: "))
num_days = int(input("Enter number of days: "))

students = []
attendance_data = {}

# Student names
for i in range(num_students):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)

# Attendance input
for day in range(1, num_days + 1):
    daily_attendance = []
    print(f"\nEnter attendance for Day {day} (P/A):")
    for student in students:
        status = input(f"{student}: ").upper()
        while status not in ['P', 'A']:
            print("Invalid input! Enter P or A only.")
            status = input(f"{student}: ").upper()
        daily_attendance.append(status)
    attendance_data[f'Day {day}'] = daily_attendance

# -----------------------------
# Step 2: Create DataFrame
# -----------------------------

df = pd.DataFrame(attendance_data, index=students)

print("\nAttendance Record:\n")
print(df)

# -----------------------------
# Step 3: Convert P/A to 1/0
# -----------------------------

attendance_numeric = df.replace({'P': 1, 'A': 0})

# -----------------------------
# Step 4: Calculate Attendance %
# -----------------------------

df['Total Present'] = attendance_numeric.sum(axis=1)
df['Attendance %'] = (df['Total Present'] / num_days) * 100

print("\nAttendance Summary:\n")
print(df[['Total Present', 'Attendance %']])

# -----------------------------
# Step 5: Visualization
# -----------------------------

plt.figure(figsize=(8, 5))
plt.bar(students, df['Attendance %'], color='lightgreen')
plt.xlabel('Students')
plt.ylabel('Attendance Percentage')
plt.title('Attendance Management System')
plt.ylim(0, 100)
plt.grid(axis='y')

plt.show()
