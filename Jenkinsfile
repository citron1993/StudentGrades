pipeline {
    agent any

    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student Name')
        string(name: 'GRADE1', defaultValue: '80', description: 'Grade 1')
        string(name: 'GRADE2', defaultValue: '90', description: 'Grade 2')
    }

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('Validate, Calculate & Generate Reports') {
            steps {
                script {
                    // קבלת פרמטרים
                    def student = params.STUDENT_NAME
                    def grade1 = params.GRADE1
                    def grade2 = params.GRADE2
                    def validInput = true
                    def avg = 0
                    def status = ""

                    // בדיקת תקינות פרמטרים
                    try {
                        grade1 = grade1.toInteger()
                        grade2 = grade2.toInteger()
                        avg = (grade1 + grade2) / 2
                        status = avg >= 50 ? "✅ PASSED" : "❌ FAILED"
                    } catch (Exception e) {
                        validInput = false
                        status = "⚠️ Invalid input! Please enter numbers for grades."
                    }

                    // יצירת דף HTML
                    writeFile file: 'report.html', text: """
                        <html>
                        <head>
                            <title>Student Grades Report</title>
                            <style>
                                body { font-family: Arial, sans-serif; background-color: #f0f2f5; padding: 20px; }
                                h1 { color: #2c3e50; }
                                .passed { color: green; font-weight: bold; }
                                .failed { color: red; font-weight: bold; }
                                .warning { color: orange; font-weight: bold; }
                                .card { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); max-width: 400px; }
                                p { font-size: 16px; }
                            </style>
                        </head>
                        <body>
                            <div class="card">
                                <h1>Student: ${student}</h1>
                                ${validInput ? """
                                    <p>Grade 1: ${grade1}</p>
                                    <p>Grade 2: ${grade2}</p>
                                    <p>Average: ${avg}</p>
                                    <p class="${avg >= 50 ? 'passed' : 'failed'}">Status: ${status}</p>
                                """ : """
                                    <p class="warning">${status}</p>
                                """}
                            </div>
                        </body>
                        </html>
                    """

                    // יצירת דף Log
                    writeFile file: 'log.html', text: """
                        <html>
                        <head><title>Build Log</title></head>
                        <body>
                            <pre>${currentBuild.rawBuild.getLog(1000).join('\n')}</pre>
                        </body>
                        </html>
                    """
                }
            }
        }
    }

    post {
        always {
            // פרסום דוחות HTML
            publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: '.', reportFiles: 'report.html', reportName: 'Student Report'])
            publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: '.', reportFiles: 'log.html', reportName: 'Build Log'])
        }

        // הבילד תמיד SUCCESS
        success {
            script { currentBuild.result = 'SUCCESS' }
        }
    }
}
