pipeline {
    agent any
    
    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student Name')
        string(name: 'GRADE1', defaultValue: '0', description: 'First Grade')
        string(name: 'GRADE2', defaultValue: '0', description: 'Second Grade')
    }

    options {
        skipDefaultCheckout()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate & Calculate') {
            steps {
                script {
                    // הגדרת שם התיקייה
                    def reportsDir = "reports"

                    // יצירת התיקייה בצורה cross-platform בעזרת dir
                    dir(reportsDir) {
                        // הבלוק הזה מבטיח שהתיקייה קיימת
                    }

                    def g1 = null
                    def g2 = null
                    def errors = []

                    // פונקציה לבדיקת ציון
                    def validateGrade = { gradeStr, name ->
                        def gradeNum = null
                        try {
                            gradeNum = gradeStr.toInteger()
                            if (gradeNum < 0 || gradeNum > 100) {
                                errors << "${name} מחוץ לטווח 0-100"
                                gradeNum = null
                            }
                        } catch (e) {
                            errors << "${name} לא מספר חוקי"
                        }
                        return gradeNum
                    }

                    g1 = validateGrade(params.GRADE1, "GRADE1")
                    g2 = validateGrade(params.GRADE2, "GRADE2")

                    def average = null
                    def status = "N/A ❌"

                    if (errors.size() == 0) {
                        average = (g1 + g2) / 2
                        status = (average >= 50) ? "PASSED ✅" : "FAILED ❌"
                    }

                    // יצירת דף HTML מעוצב
                    def htmlContent = """
                    <html>
                    <head>
                        <title>Grade Report</title>
                        <style>
                            body { font-family: Arial; background: #f4f4f4; padding: 20px; }
                            h1 { color: #333; }
                            table { border-collapse: collapse; width: 50%; }
                            td, th { border: 1px solid #999; padding: 10px; text-align: center; }
                            .passed { color: green; font-weight: bold; }
                            .failed { color: red; font-weight: bold; }
                            .error { color: orange; font-weight: bold; }
                        </style>
                    </head>
                    <body>
                        <h1>Grade Report for ${params.STUDENT_NAME}</h1>
                        <table>
                            <tr><th>Grade 1</th><th>Grade 2</th><th>Average</th><th>Status</th></tr>
                            <tr>
                                <td>${g1 != null ? g1 : "-"}</td>
                                <td>${g2 != null ? g2 : "-"}</td>
                                <td>${average != null ? average : "-"}</td>
                                <td class="${errors.size() > 0 ? 'error' : (average != null && average >= 50 ? 'passed' : 'failed')}">
                                    ${errors.size() > 0 ? "ERROR ❌" : status}
                                </td>
                            </tr>
                        </table>
                        ${errors.size() > 0 ? "<p style='color:red;'>Errors: ${errors.join(', ')}</p>" : ""}
                    </body>
                    </html>
                    """
                    
                    // כתיבת הקבצים לנתיב היחסי
                    writeFile file: "${reportsDir}/GradeReport.html", text: htmlContent

                    def logContent = """
                    <html>
                    <head><title>Build Log</title></head>
                    <body>
                    <h1>Build Log</h1>
                    <pre>
Student: ${params.STUDENT_NAME}
Grade 1: ${g1 != null ? g1 : "-"}
Grade 2: ${g2 != null ? g2 : "-"}
Average: ${average != null ? average : "-"}
Status: ${errors.size() > 0 ? "ERROR ❌" : status}
Errors: ${errors.join(', ')}
                    </pre>
                    </body>
                    </html>
                    """
                    writeFile file: "${reportsDir}/BuildLog.html", text: logContent

                    echo "Grade Report: ${env.BUILD_URL}artifact/${reportsDir}/GradeReport.html"
                    echo "Build Log: ${env.BUILD_URL}artifact/${reportsDir}/BuildLog.html"
                }
            }
        }
    }

    post {
        always {
            // ארכוב הקבצים מהתיקייה
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}
