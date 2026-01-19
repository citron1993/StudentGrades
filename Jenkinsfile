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
                    // יצירת תיקיות לדוחות
                    def reportsDir = "${env.WORKSPACE}/reports"

                    if (isUnix()) {
                        sh "mkdir -p ${reportsDir}"
                    } else {
                        bat "mkdir \"${reportsDir}\""
                    }

                    // בדיקה אם הקלט תקין
                    def g1 = 0
                    def g2 = 0
                    def errors = []
                    try { g1 = params.GRADE1.toInteger() } catch (e) { errors << "GRADE1 לא חוקי" }
                    try { g2 = params.GRADE2.toInteger() } catch (e) { errors << "GRADE2 לא חוקי" }

                    def average = (g1 + g2) / 2
                    def status = (average >= 50) ? "PASSED ✅" : "FAILED ❌"

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
                        </style>
                    </head>
                    <body>
                        <h1>Grade Report for ${params.STUDENT_NAME}</h1>
                        <table>
                            <tr><th>Grade 1</th><th>Grade 2</th><th>Average</th><th>Status</th></tr>
                            <tr>
                                <td>${g1}</td>
                                <td>${g2}</td>
                                <td>${average}</td>
                                <td class="${average>=50?'passed':'failed'}">${status}</td>
                            </tr>
                        </table>
                        ${errors.size() > 0 ? "<p style='color:red;'>Errors: ${errors.join(', ')}</p>" : ""}
                    </body>
                    </html>
                    """
                    writeFile file: "${reportsDir}/GradeReport.html", text: htmlContent

                    // יצירת דף HTML ללוג
                    def logContent = """
                    <html>
                    <head><title>Build Log</title></head>
                    <body>
                    <h1>Build Log</h1>
                    <pre>
                    Student: ${params.STUDENT_NAME}
                    Grade 1: ${g1}
                    Grade 2: ${g2}
                    Average: ${average}
                    Status: ${status}
                    Errors: ${errors.join(', ')}
                    </pre>
                    </body>
                    </html>
                    """
                    writeFile file: "${reportsDir}/BuildLog.html", text: logContent

                    // שמירת לינק ל־Console
                    echo "Grade Report: ${env.BUILD_URL}artifact/reports/GradeReport.html"
                    echo "Build Log: ${env.BUILD_URL}artifact/reports/BuildLog.html"
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}
