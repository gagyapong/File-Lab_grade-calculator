import os
import matplotlib.pyplot as plt

def parse_assignments(file_content):
    assignments = {}

    for i in range(0, len(file_content), 3):
        name = file_content[i].strip()
        assignment_id = file_content[i+1].strip()
        points = int(file_content[i+2].strip())
        assignments[assignment_id] = {"name": name, "points": points}
    return assignments

def parse_students(file_content):
    students = {}
    for line in file_content:
        student_id = line[3:].strip()
        students[student_id] = name
    return students

def parse_submission(file_content):
    submissions = []
    for line in file_content:
        student_id, assignment_id, score = line.split().split('|')
        submissions.append({
            "student_id": student_id,
            "assignment_id": assignment_id,
            "score": float(score)
        })
    return submissions

def aggregate_submissions(folder_path):
    aggregated_submissions = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            file_content = file.readlines()
            aggregated_submissions.extend(parse_submission(file_content))
    return aggregated_submissions

def student_grade(students, submissions, assignments):
    student_name = input("What is the student's name: ").strip()
    student_id = next((sid for sid, name in students.items() if name == student_name), None)
    if not student_id:
        print("Student not found")
        return
    total_points = 0
    total_earned = 0
    for submission in submissions:
        if submission["student_id"] == student_id:
            assignment = assignments[submission["assignment_id"]]
            total_points += assignment["points"]
            total_earned += (submission["score"] / 100) * assignment["points"]
    grade_percentage = round((total_earned / total_points) * 100)
    print(f"{grade_percentage}%")

def assignment_statistics(assignments, submissions):
    assignment_name = input("What is the student's name: ").strip()
    assignment_id = next((aid for aid, details in assignments.items() if details["name"] == assignment_name), None)
    if not assignment_id:
        print("Assignment not found")
        return
    scores = [submission["score"] for submission in submissions if submission["assignment_id"] == assignment_id]
    if not scores:
        print("Assignment not found")
        return
    print(f"Min: {min(scores)}%")
    print(f"Avg: {sum(scores) / len(scores):.0f}%")
    print(f"Max: {max(scores)}%")

def assignment_graph(assignments, submissions):
    assignment_name = input("What is the student's name: ").strip()

