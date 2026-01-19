pipeline {
    agent any

    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student name')
        string(name: 'GRADE1', defaultValue: '50', description: 'First grade')
        string(name: 'GRADE2', defaultValue: '40', description: 'Second grade')
    }

    stages {
        stage('Calculate & Generate Report') {
            steps {
                script {
                    int g1 = params.GRADE1.toInteger()
                    int g2 = params.GRADE2.toInteger()
                    int avg = (g1 + g2) / 2

                    currentBuild.result = (avg >= 60) ? 'SUCCESS' : 'FAILURE'

                    def status = avg >= 60 ? "PASSED ✅" : "FAILED ❌"
                    def color  = avg >= 60 ? "#2ecc71" : "#e74c3c"

                    writeFile file: 'report.html', text: """
<html>
<head>
<style>
body {
 background:#f4f6f8;
 font-family:Arial;
}
.card {
 width:420px;
 margin:50px auto;
 background:white;
 padding:25px;
 border-radius:14px;
 box-shadow:0 6px 14px rgba(0,0,0,0.15);
}
.status {
 background:${color};
 color:white;
 padding:12px;
 text-align:center;
 border-radius:8px;
 font-size:22px;
 margin-top:15px;
}
</style>
</head>
<body>
<div class="card">
<h2>📘 Student Grades Report</h2>
<p><b>Name:</b> ${params.STUDENT_NAME}</p>
<p><b>Grade 1:</b> ${g1}</p>
<p><b>Grade 2:</b> ${g2}</p>
<p><b>Average:</b> ${avg}</p>
<div class="status">${status}</div>
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
