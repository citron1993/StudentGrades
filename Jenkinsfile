pipeline {
    agent none  // חשוב: לא להגדיר Node ברמת Pipeline, נעבור ל-stage לפי פרמטר

    // ---------- פרמטרים ----------
    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student Name')
        string(name: 'GRADE1', defaultValue: '85', description: 'Grade 1')
        string(name: 'GRADE2', defaultValue: '90', description: 'Grade 2')
        booleanParam(name: 'PASSED_EXAM', defaultValue: true, description: 'Passed Exam')
        string(name: 'EXAM_DATE', defaultValue: '2024-12-01', description: 'Exam Date (YYYY-MM-DD)')

        // ---------- בחירת מערכת הפעלה ----------
        choice(name: 'NODE', choices: ['master', 'linux'], description: 'בחר מערכת הפעלה להרצה')
    }

    stages {
        stage('Run Script') {
            agent { label "${params.NODE}" }  // שולח את הבילד ל־Node שבחרת

            steps {
                echo "Running on node: ${params.NODE}"

                script {
                    if (params.NODE == 'master') {
                        // 🔹 הרצה על Windows
                        bat """
                            "C:\\Users\\citro\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" ^
                            grades_calculator.py ^
                            %STUDENT_NAME% %GRADE1% %GRADE2% %PASSED_EXAM% %EXAM_DATE%
                        """
                    } else {
                        // 🔹 הרצה על Linux
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

        stage('Archive Results') {
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
