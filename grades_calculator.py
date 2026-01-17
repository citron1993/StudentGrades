import sys
from datetime import datetime

error_message = None
final_status = "UNKNOWN"

# ---------- בדיקת מספר פרמטרים ----------
if len(sys.argv) != 6:
    error_message = "Invalid number of arguments"

else:
    student_name = sys.argv[1]
    grade1_raw = sys.argv[2]
    grade2_raw = sys.argv[3]
    passed_exam_raw = sys.argv[4].lower()
    exam_date_raw = sys.argv[5]

    # ---------- ולידציה ציונים ----------
    try:
        grade1 = int(grade1_raw)
        grade2 = int(grade2_raw)
        if not (0 <= grade1 <= 100 and 0 <= grade2 <= 100):
            error_message = "Grades must be between 0 and 100"
    except ValueError:
        error_message = "Grades must be numbers"

    # ---------- ולידציה Boolean ----------
    if not error_message:
        if passed_exam_raw == "true":
            passed_exam = True
        elif passed_exam_raw == "false":
            passed_exam = False
        else:
            error_message = "passed_exam must be true or false"

    # ---------- ולידציה תאריך ----------
    if not error_message:
        try:
            exam_date = datetime.strptime(exam_date_raw, "%Y-%m-%d")
        except ValueError:
            error_message = "exam_date must be in YYYY-MM-DD format"

    # ---------- חישוב ----------
    if not error_message:
        average = (grade1 + grade2) / 2
        final_status = "PASS" if passed_exam and average >= 60 else "FAIL"
    else:
        average = "N/A"
        final_status = "INVALID INPUT"

# ---------- יצירת HTML ----------
html_content = f"""
<html>
<head><title>Student Grade Report</title></head>
<body>
<h1>Student Grade Report</h1>
<p><strong>Status:</strong> {final_status}</p>
<p><strong>Error:</strong> {error_message or "None"}</p>
</body>
</html>
"""

with open("result.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# ---------- יצירת LOG ----------
log_content = f"""
Status: {final_status}
Error: {error_message}
Run Time: {datetime.now()}
"""

with open("script.log", "w", encoding="utf-8") as f:
    f.write(log_content)

print("Script finished successfully")
