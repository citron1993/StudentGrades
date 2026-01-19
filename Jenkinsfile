pipeline {
    agent any

    parameters {
        string(name: 'STUDENT', defaultValue: 'David', description: 'Student Name')
        string(name: 'GRADE1', defaultValue: '80', description: 'First Grade')
        string(name: 'GRADE2', defaultValue: '90', description: 'Second Grade')
    }

    stages {
        stage('Validate & Calculate') {
            steps {
                script {
                    def logText = ""
                    def htmlText = ""
                    def status = ""
                    def avg = 0

                    try {
                        // המרה ל־Integer
                        def g1 = params.GRADE1.toInteger()
                        def g2 = params.GRADE2.toInteger()

                        avg = (g1 + g2) / 2
                        logText += "Student: ${params.STUDENT}<br>"
                        logText += "Grade 1: ${g1}<br>"
                        logText += "Grade 2: ${g2}<br>"
                        logText += "Average: ${avg}<br>"

                        if (avg >= 50) {
                            status = "✅ PASSED"
                            logText += "<span style='color:green'>Status: ${status}</span><br>"
                        } else {
                            status = "❌ FAILED"
                            logText += "<span style='color:red'>Status: ${status}</span><br>"
                        }

                    } catch(Exception e) {
                        status = "⚠️ Invalid input!"
                        logText += "<span style='color:orange'>${status}</span><br>"
                    }

                    // יצירת דף HTML לתוצאה
                    htmlText += """
                    <html>
                    <head>
                        <title>Grade Report</title>
                        <style>
                            body { font-family: Arial; background:#f2f2f2; padding:20px; }
                            .card { background:white; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.2); max-width:400px; margin:auto; }
                            h2 { color:#333; }
                            .passed { color: green; font-weight:bold; }
                            .failed { color: red; font-weight:bold; }
                            .warning { color: orange; font-weight:bold; }
                        </style>
                    </head>
                    <body>
                        <div class="card">
                            <h2>Student: ${params.STUDENT}</h2>
                            <p>Grade 1: ${params.GRADE1}</p>
                            <p>Grade 2: ${params.GRADE2}</p>
                            <p>Average: ${avg}</p>
                            <p>Status: ${
                                status.contains('PASSED') ? '<span class="passed">' + status + '</span>' :
                                status.contains('FAILED') ? '<span class="failed">' + status + '</span>' :
                                '<span class="warning">' + status + '</span>'
                            }</p>
                        </div>
                    </body>
                    </html>
                    """

                    // שמירת קבצי HTML
                    writeFile file: 'grade_report.html', text: htmlText
                    writeFile file: 'log.html', text: "<html><body>${logText}</body></html>"
                }
            }
        }
    }

    post {
        always {
            script {
                // תמיד SUCCESS
                currentBuild.result = 'SUCCESS'
            }

            // פרסום דפי HTML
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'grade_report.html',
                reportName: 'Grade Report'
            ])

            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'log.html',
                reportName: 'Build Log'
            ])
        }
    }
}
