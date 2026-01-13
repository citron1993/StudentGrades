pipeline {
    // Agent can be any, we will choose OS per stage
    agent none

    // Parameters for the script
    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student Name')
        string(name: 'GRADE1', defaultValue: '85', description: 'Grade 1')
        string(name: 'GRADE2', defaultValue: '90', description: 'Grade 2')
        booleanParam(name: 'PASSED_EXAM', defaultValue: true, description: 'Passed Exam')
        string(name: 'EXAM_DATE', defaultValue: '2024-12-01', description: 'Exam Date (YYYY-MM-DD)')
        choice(name: 'TARGET_OS', choices: ['Windows', 'Linux'], description: 'Select OS to run the script')
    }

    stages {
        stage('Run Script') {
            steps {
                script {
                    if (params.TARGET_OS == 'Windows') {
                        // Windows Node
                        bat "C:\\Users\\citro\\AppData\\Local\\Programs\\Python\\Python313\\python.exe grades_calculator.py %STUDENT_NAME% %GRADE1% %GRADE2% %PASSED_EXAM% %EXAM_DATE%"
                    } else {
                        // Linux Node (WSL or Linux machine)
                        sh "python3 grades_calculator.py ${STUDENT_NAME} ${GRADE1} ${GRADE2} ${PASSED_EXAM} ${EXAM_DATE}"
                    }
                }
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'result.html, script.log', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check the logs and HTML report."
        }
    }
}
