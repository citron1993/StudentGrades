pipeline {
    agent none  // חשוב: בלי זה החלונית של Build with Parameters לא תופיע

    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student Name')
        string(name: 'GRADE1', defaultValue: '85', description: 'Grade 1')
        string(name: 'GRADE2', defaultValue: '90', description: 'Grade 2')
        booleanParam(name: 'PASSED_EXAM', defaultValue: true, description: 'Passed Exam')
        string(name: 'EXAM_DATE', defaultValue: '2024-12-01', description: 'Exam Date (YYYY-MM-DD)')
        choice(
            name: 'NODE',
            choices: ['master','linux'],  // חייב להתאים ל-label של ה-Nodes
            description: 'בחר מערכת הפעלה להרצה'
        )
    }

    stages {
        stage('Checkout from GitHub') {
            agent { label "${params.NODE}" }
            steps {
                echo "Running on node: ${params.NODE}"
                checkout([$class: 'GitSCM', 
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/itaycitron/StudentGrades.git']]
                ])
            }
        }

        stage('Run Grades Calculator') {
            agent { label "${params.NODE}" }
            steps {
                script {
                    // בחר איך להריץ בהתאם ל־Node
                    if (params.NODE == 'master') {
                        echo 'Running Python script on Windows'
                        bat """
                        "C:\\Users\\citro\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" ^
                        grades_calculator.py ^
                        %STUDENT_NAME% %GRADE1% %GRADE2% %PASSED_EXAM% %EXAM_DATE%
                        """
                    } else {
                        echo 'Running Python script on Linux'
                        sh """
                        python3 grades_calculator.py \
                        ${STUDENT_NAME} \
                        ${GRADE1} \
                        ${GRADE2} \
                        ${PASSED_EXAM} \
                        ${EXAM_DATE}
                        """
                    }
                }
            }
        }

        stage('Compute Average and Update Report') {
            agent { label "${params.NODE}" }
            steps {
                script {
                    // חישוב ממוצע והכנת סטטוס סופי
                    def grade1 = params.GRADE1.toInteger()
                    def grade2 = params.GRADE2.toInteger()
                    def passed = params.PASSED_EXAM
                    def average = (grade1 + grade2) / 2
                    def final_status = (passed && average >= 60) ? "PASS" : "FAIL"

                    // שמירת HTML
                    writeFile file: 'result.html', text: """
                    <html>
                    <head><title>Student Grade Report</title></head>
                    <body>
                    <h1>Student Grade Report</h1>
                    <p><strong>Name:</strong> ${params.STUDENT_NAME}</p>
                    <p><strong>Grade 1:</strong> ${grade1}</p>
                    <p><strong>Grade 2:</strong> ${grade2}</p>
                    <p><strong>Average:</strong> ${average}</p>
                    <p><strong>Passed Exam:</strong> ${passed}</p>
                    <p><strong>Status:</strong> ${final_status}</p>
                    </body>
                    </html>
                    """

                    // שמירת log
                    writeFile file: 'script.log', text: """
                    Student: ${params.STUDENT_NAME}
                    Grade 1: ${grade1}
                    Grade 2: ${grade2}
                    Average: ${average}
                    Passed Exam: ${passed}
                    Final Status: ${final_status}
                    Run Time: ${new Date()}
                    """
                }
            }
        }

        stage('Archive Results') {
            agent { label "${params.NODE}" }
            steps {
                archiveArtifacts artifacts: 'result.html, script.log', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully'
        }
        failure {
            echo 'Pipeline failed – check console output'
        }
    }
}
