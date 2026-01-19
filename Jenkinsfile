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
                    // כל השגיאות יתפסו פה, אבל הבילד לא ייפול
                    catchError(buildResult: 'SUCCESS') {
                        try {
                            def grade1 = params.GRADE1.toInteger()
                            def grade2 = params.GRADE2.toInteger()
                            def avg = (grade1 + grade2) / 2

                            echo "Student: ${params.STUDENT}"
                            echo "Grade 1: ${grade1}"
                            echo "Grade 2: ${grade2}"
                            echo "Average: ${avg}"

                            def status = avg >= 50 ? "✅ PASSED" : "❌ FAILED"
                            echo status

                            // כתיבת HTML
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
                            publishHTML(target: [
                                allowMissing: false,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: '.',
                                reportFiles: 'report.html',
                                reportName: 'Student Report'
                            ])

                        } catch (Exception e) {
                            echo "⚠️ ERROR: Invalid input parameters!"
                        }
                    }
                }
            }
        }
    }
}
