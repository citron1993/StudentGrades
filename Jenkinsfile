pipeline {
    agent none   // חשוב: בלי זה לא תופיע חלונית

    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student Name')
        string(name: 'GRADE1', defaultValue: '85', description: 'Grade 1')
        string(name: 'GRADE2', defaultValue: '90', description: 'Grade 2')
        booleanParam(name: 'PASSED_EXAM', defaultValue: true, description: 'Passed Exam')
        string(name: 'EXAM_DATE', defaultValue: '2024-12-01', description: 'Exam Date (YYYY-MM-DD)')
    }

    stages {
        stage('Run on Master and Agent') {
            matrix {

                // 🔹 זה מה שיוצר את החלונית
                axes {
                    axis {
                        name 'NODE'
                        values 'master', 'agent'
                    }
                }

                // 🔹 בחירת ה־Node לפי label
                agent { label NODE }

                stages {

                    stage('Checkout from GitHub') {
                        steps {
                            checkout scm
                        }
                    }

                    stage('Run Script') {
                        steps {
                            echo "Running on node: ${NODE}"

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

                    stage('Archive Results') {
                        steps {
                            archiveArtifacts artifacts: 'result.html, script.log', fingerprint: true
                        }
                    }
                }
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


