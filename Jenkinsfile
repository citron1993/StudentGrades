pipeline {
    agent { label 'linux' } // מריץ על Node של Linux

    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student Name')
        string(name: 'GRADE1', defaultValue: '85', description: 'Grade 1')
        string(name: 'GRADE2', defaultValue: '90', description: 'Grade 2')
        booleanParam(name: 'PASSED_EXAM', defaultValue: true, description: 'Passed Exam')
        string(name: 'EXAM_DATE', defaultValue: '2024-12-01', description: 'Exam Date (YYYY-MM-DD)')
    }

    stages {
        stage('Prepare Workspace') {
            steps {
                echo "Cleaning workspace and preparing for build"
                sh 'rm -f result.html script.log || true'
            }
        }

        stage('Run Grades Calculator') {
            steps {
                echo "Running Python script on Linux node"

                sh """
                python3 - << 'EOF'
import sys
from datetime import datetime

# קריאת פרמטרים מהסביבה של Jenkins
student_name = '${STUDENT_NAME}'
grade1 = int('${GRADE1}')
grade2 = int('${GRADE2}')
passed_exam = '${PASSED_EXAM}' == 'true'
exam_date_raw = '${EXAM_DATE}'

# חישוב ממוצע
average = (grade1 + grade2) / 2
final_status = 'PASS' if passed_exam and average >= 60 else 'FAIL'

# יצירת HTML
html_content = f\"\"\"
<html>
<head><title>Student Grade Report</title></head>
<body>
<h1>Student Grade Report</h1>
<p><strong>Student:</strong> {student_name}</p>
<p><strong>Grade 1:</strong> {grade1}</p>
<p><strong>Grade 2:</strong> {grade2}</p>
<p><strong>Average:</strong> {average}</p>
<p><strong>Exam Date:</strong> {exam_date_raw}</p>
<p><strong>Status:</strong> {final_status}</p>
</body>
</html>
\"\"\"

with open("result.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# יצירת log
log_content = f"Student: {student_name}\\nGrade1: {grade1}\\nGrade2: {grade2}\\nAverage: {average}\\nPassed Exam: {passed_exam}\\nStatus: {final_status}\\nRun Time: {datetime.now()}\\n"

with open("script.log", "w", encoding="utf-8") as f:
    f.write(log_content)

print("Python script finished successfully")
EOF
                """
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'result.html, script.log', fingerprint: true
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully ✅' }
        failure { echo 'Pipeline failed – check console output ❌' }
    }
}
