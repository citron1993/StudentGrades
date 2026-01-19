pipeline {
    agent any

    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student name')
        string(name: 'GRADE1', defaultValue: '50', description: 'First grade (0-100)')
        string(name: 'GRADE2', defaultValue: '40', description: 'Second grade (0-100)')
    }

    stages {
        stage('Validate, Calculate & Report') {
            steps {
                script {

                    def errorMessage = ""
                    def statusText = ""
                    def statusColor = "#3498db"
                    def avgText = "-"

                    try {
                        int g1 = params.GRADE1.toInteger()
                        int g2 = params.GRADE2.toInteger()

                        if (g1 < 0 || g1 > 100 || g2 < 0 || g2 > 100) {
                            errorMessage = "❗ Grades must be between 0 and 100"
                            currentBuild.result = 'UNSTABLE'
                        } else {
                            int avg = (g1 + g2) / 2
                            avgText = avg.toString()

                            if (avg >= 60) {
                                statusText = "PASSED ✅"
                                statusColor = "#2ecc71"
                                currentBuild.result = 'SUCCESS'
                            } else {
                                statusText = "FAILED ❌"
                                statusColor = "#e74c3c"
                                currentBuild.result = 'UNSTABLE'
                            }
                        }

                    } catch (Exception e) {
                        errorMessage = "❗ Invalid input – grades must be numbers"
                        currentBuild.result = 'UNSTABLE'
                    }

                    writeFile file: 'report.html', text: """
<html>
<head>
<style>
body {
 background:#f4f6f8;
 font-family:Arial;
}
.card {
 width:450px;
 margin:50px auto;
 background:white;
 padding:25px;
 border-radius:14px;
 box-shadow:0 6px 14px rgba(0,0,0,0.15);
}
.status {
 background:${statusColor};
 color:white;
 padding:12px;
 text-align:center;
 border-radius:8px;
 font-size:22px;
 margin-top:15px;
}
.error {
 background:#f39c12;
 color:white;
 padding:12px;
 border-radius:8px;
 margin-top:15px;
}
</style>
</head>
<body>
<div class="card">
<h2>📘 Student Grades Report</h2>

<p><b>Name:</b> ${params.STUDENT_NAME}</p>
<p><b>Grade 1:</b> ${params.GRADE1}</p>
<p><b>Grade 2:</b> ${params.GRADE2}</p>
<p><b>Average:</b> ${avgText}</p>

${statusText ? "<div class='status'>${statusText}</div>" : ""}
${errorMessage ? "<div class='error'>${errorMessage}</div>" : ""}

</div>
</body>
</html>
"""
                }
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Student Grades Report',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])
        }
    }
}
