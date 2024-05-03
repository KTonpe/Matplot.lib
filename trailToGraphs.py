import json
import matplotlib.pyplot as plt
import mpld3

MARKS_FILE_PATH = r'C:\Users\1038589\OneDrive - Blue Yonder\Training modules\Data to Graphs in python\StudentMarks.json'
def read_from_file():
    with open(MARKS_FILE_PATH,'r') as file:
        data = json.load(file)
        return data
    
def display_marks_by_name():
    name = input("Enter the name of the student: ")
    for student in data:
        if student['name'] == name:
            print(student)
            break
    else:
        print("Student not found")
if __name__ == "__main__":
    data = read_from_file()
    subjects = list(data[0]["marks"].keys())
    marks = {student["name"]: list(student["marks"].values()) for student in data}

    # Plotting
    plt.figure(figsize=(10, 6))

    for student, student_marks in marks.items():
        plt.plot(subjects, student_marks, marker='o', label=student)

    plt.title('Marks Obtained by Students')
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.xticks(subjects, rotation=45)  # Set custom x-axis tick labels
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


