pipeline {
    agent any

    parameters {
        string(name: 'STUDENT', defaultValue: 'David', description: 'Student name')
        string(name: 'GRADE1', defaultValue: '80', description: 'First grade')
        string(name: 'GRADE2', defaultValue: '90', description: 'Second grade')
    }

    stages {
        stage('Calculate & Report') {
            steps {
                script {
                    // משתנה לשמירת כל הלוג
                    def logContent = ""

                    // לא שובר את הבילד אם יש שגיאה
                    catchError(buildResult: 'SUCCESS') {
                        try {
                            def grade1 = params.GRADE1.toInteger()
                            def grade2 = params.GRADE2.toInteger()
                            def avg = (grade1 + grade2) / 2

                            logContent += "Student: ${params.STUDENT}\n"
                            logContent += "Grade 1: ${grade1}\n"
                            logContent += "Grade 2: ${grade2}\n"
                            logContent += "Average: ${avg}\n"

                            def status = avg >= 50 ? "✅ PASSED" : "❌ FAILED"
                            logContent += "${status}\n"

                            // HTML של דוח תוצאות
                            def html = """
                            <html>
                            <head>
                                <style>
                                    body { font-family: Arial; }
                                    .passed { color: green; }
                                    .failed { color: red; }
                                </style>
                            </head>
                            <body>
                                <h2>Student Report</h2>
                                <p>Name: ${params.STUDENT}</p>
                                <p>Grade 1: ${grade1}</p>
                                <p>Grade 2: ${grade2}</p>
                                <p>Average: ${avg}</p>
                                <p class="${avg>=50 ? 'passed' : 'failed'}">${status}</p>
                            </body>
                            </html>
                            """
                            writeFile file: 'report.html', text: html

                            // HTML של לוג
                            def logHtml = """
                            <html>
                            <head>
                                <style>
                                    body { font-family: monospace; white-space: pre; }
                                    .error { color: red; }
                                </style>
                            </head>
                            <body>
                                <h2>Build Log</h2>
                                <pre>${logContent}</pre>
                            </body>
                            </html>
                            """
                            writeFile file: 'log.html', text: logHtml

                            // פרסום שני הדפים
                            publishHTML(target: [
                                allowMissing: false,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: '.',
                                reportFiles: 'report.html',
                                reportName: 'Student Report'
                            ])
                            publishHTML(target: [
                                allowMissing: false,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: '.',
                                reportFiles: 'log.html',
                                reportName: 'Build Log'
                            ])

                        } catch (Exception e) {
                            logContent += "⚠️ ERROR: Invalid input parameters!\n"
                            echo "⚠️ ERROR: Invalid input parameters!"
                        }
                    }
                }
            }
        }
    }
}
