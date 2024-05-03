import json

READ_FROM_MARKS_FILE_PATH = r'C:\Users\1038589\OneDrive - Blue Yonder\Training modules\Data to Graphs in python\StudentMarks.json'

def read_from_file():
    with open(READ_FROM_MARKS_FILE_PATH, 'r') as f:
        data = json.load(f)
        return data
    
def Find_average_marks_of_subject():
    # Initialize dictionary to store total marks for each subject
    subject_total_marks = {subject: 0 for subject in Student_data[0]["marks"].keys()}
    # Count number of students
    num_students = len(Student_data)

    # Calculate total marks for each subject
    for student in Student_data:
        marks = student["marks"]
        for subject, mark in marks.items():
            subject_total_marks[subject] += mark

    # Calculate average marks for each subject
    average_marks = {subject: total_marks / num_students for subject, total_marks in subject_total_marks.items()}

    print("Average marks obtained in each subject:")
    print(average_marks)
if __name__ == '__main__':
    Student_data = read_from_file()
    Find_average_marks_of_subject()
