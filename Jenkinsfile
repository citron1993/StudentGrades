pipeline {
    agent none   // חשוב! אחרת Node קבוע מונע את החלונית

    // ---------- פרמטרים ----------
    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student Name')
        string(name: 'GRADE1', defaultValue: '85', description: 'Grade 1')
        string(name: 'GRADE2', defaultValue: '90', description: 'Grade 2')
        booleanParam(name: 'PASSED_EXAM', defaultValue: true, description: 'Passed Exam')
        string(name: 'EXAM_DATE', defaultValue: '2024-12-01', description: 'Exam Date (YYYY-MM-DD)')

        // ---------- בחירת Node / מערכת הפעלה ----------
        choice(
            name: 'NODE',
            choices: ['master', 'linux'],  // חייב להתאים ל-label של ה-Nodes שלך
            description: 'בחר מערכת הפעלה להרצה'
        )
    }

    stages {
        stage('Run Script') {
            // שולח את הבילד ל־Node שבחר המשתמש
            agent { label "${params.NODE}" }

            steps {
                echo "Running on node: ${params.NODE}"

                script {
                    if (params.NODE == 'master') {
                        // 🔹 Windows
                        bat """
                            "C:\\Users\\citro\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" ^
                            grades_calculator.py ^
                            %STUDENT_NAME% %GRADE1% %GRADE2% %PASSED_EXAM% %EXAM_DATE%
                        """
                    } else {
                        // 🔹 Linux
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
