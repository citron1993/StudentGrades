pipeline {
    agent none

    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student Name')
        string(name: 'GRADE1', defaultValue: '85', description: 'Grade 1')
        string(name: 'GRADE2', defaultValue: '90', description: 'Grade 2')
        booleanParam(name: 'PASSED_EXAM', defaultValue: true, description: 'Passed Exam')
        string(name: 'EXAM_DATE', defaultValue: '2024-12-01', description: 'Exam Date (YYYY-MM-DD)')
        choice(
            name: 'NODE',
            choices: ['master','linux'],
            description: 'בחר מערכת הפעלה להרצה'
        )
    }

    stages {
        stage('Checkout & Run Script') {
            steps {
                script {
                    echo "Running on node: ${params.NODE}"

                    if (params.NODE == 'master') {
                        node('master') {
                            checkout scm
                            bat """
                                "C:\\Users\\citro\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" ^
                                grades_calculator.py ^
                                %STUDENT_NAME% %GRADE1% %GRADE2% %PASSED_EXAM% %EXAM_DATE%
                            """
                        }
                    } else {
                        node('linux') {
                            checkout scm
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

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'result.html, script.log', fingerprint: true
            }
        }
    }
}
