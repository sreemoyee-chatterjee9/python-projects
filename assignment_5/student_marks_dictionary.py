student_marks = {
    "Aarav": 88,
    "Vivaan": 92,
    "Aditya": 76,
    "Arjun": 85,
    "Krishna": 90,
    "Ishaan": 79,
    "Anaya": 95,
    "Diya": 87,
    "Meera": 91,
    "Sneha": 82,
    "Riya": 89,
    "Priya": 78,
    "Rahul": 84,
    "Karthik": 80,
    "Siddharth": 86
}

try:
    user_enquiry=input("Enter the student's name: ").capitalize()
    score=student_marks[user_enquiry]
    print(f"{user_enquiry}'s marks : {score}")
except KeyError:
    print("Student Not Found!")
