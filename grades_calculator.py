import sys
from datetime import datetime

# ---------- בדיקת מספר פרמטרים ----------
if len(sys.argv) != 6:
    print("Usage: python grades_calculator.py <name> <grade1> <grade2> <passed_exam> <exam_date>")
    sys.exit(1)

# ---------- קבלת פרמטרים ----------
student_name = sys.argv[1]
grade1_raw = sys.argv[2]
grade2_raw = sys.argv[3]
passed_exam_raw = sys.argv[4].lower()
exam_date_raw = sys.argv[5]

# ---------- ולידציה והמרת ציונים ----------
try:
    grade1 = int(grade1_raw)
    grade2 = int(grade2_raw)
except ValueError:
    print("Error: Grades must be numbers")
    sys.exit(1)

if not (0 <= grade1 <= 100 and 0 <= grade2 <= 100):
    print("Error: Grades must be between 0 and 100")
    sys.exit(1)

# ---------- ולידציה והמרת Boolean ----------
if passed_exam_raw == "true":
    passed_exam = True
elif passed_exam_raw == "false":
    passed_exam = False
else:
    print("Error: passed_exam must be true or false")
    sys.exit(1)

# ---------- ולידציה והמרת תאריך ----------
try:
    exam_date = datetime.strptime(exam_date_raw, "%Y-%m-%d")
except ValueError:
    print("Error: exam_date must be in YYYY-MM-DD format")
    sys.exit(1)

# ---------- חישוב ----------
average = (grade1 + grade2) / 2

if passed_exam and average >= 60:
    final_status = "PASS"
else:
    final_status = "FAIL"

# ---------- יצירת קובץ HTML ----------
html_content = f"""
<html>
<head>
    <title>Student Grade Report</title>
</head>
<body>
    <h1>Student Grade Report</h1>
    <p><strong>Name:</strong> {student_name}</p>
    <p><strong>Grade 1:</strong> {grade1}</p>
    <p><strong>Grade 2:</strong> {grade2}</p>
    <p><strong>Average:</strong> {average}</p>
    <p><strong>Exam Date:</strong> {exam_date.date()}</p>
    <h2>Status: {final_status}</h2>
</body>
</html>
"""

with open("result.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML report generated: result.html")
# ---------- יצירת קובץ LOG ----------
log_content = f"""
Student Name: {student_name}
Grade 1: {grade1}
Grade 2: {grade2}
Average: {average}
Exam Date: {exam_date.date()}
Passed Exam: {passed_exam}
Final Status: {final_status}
Run Time: {datetime.now()}
"""

with open("script.log", "w", encoding="utf-8") as log_file:
    log_file.write(log_content)

print("Log file generated: script.log")
        