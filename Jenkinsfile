pipeline {
    agent none  // חייב להיות none כדי שהחלונית תופיע

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
        stage('Checkout') {
            steps {
                echo "Running on node: ${params.NODE}"
                checkout scm
            }
        }

        stage('Run Script') {
            steps {
                script {
                    if (params.NODE == 'master') {
                        node('master') {
                            bat """
                                "C:\\Users\\citro\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" ^
                                grades_calculator.py ^
                                %STUDENT_NAME% %GRADE1% %GRADE2% %PASSED_EXAM% %EXAM_DATE%
                            """
                        }
                    } else {
                        node('linux') {
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
        }

        stage('Archive') {
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
