working_days = int(input("Enter working days: "))
absent = int(input("Absent days: "))

attendance = 100 - (absent * 100 / working_days)
print(f"Your attendance: %{round(attendance)}")

if attendance < 75:
    print("Bad!")
else:
    print("Good!")