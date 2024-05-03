import json

READ_FROM_MARKS_FILE_PATH = r'C:\Users\1038589\OneDrive - Blue Yonder\Training modules\Data to Graphs in python\StudentMarks.json'

def read_from_file():
    with open(READ_FROM_MARKS_FILE_PATH, 'r') as f:
        data = json.load(f)
        return data
    
def Find_average_marks_by_student():
    # Calculate average marks for each student
    average_marks = []
    for student in Student_data:
        name = student["name"]
        marks = student["marks"]
        total_marks = sum(marks.values())
        subjects_count = len(marks)
        average_mark = total_marks / subjects_count
        average_marks.append((name, average_mark))

    print("Average marks obtained by every student in all subjects:")
    print(average_marks)

if __name__ == '__main__':
    Student_data = read_from_file()
    Find_average_marks_by_student()