pipeline {
    agent any

    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student name')
        string(name: 'GRADE1', defaultValue: '80', description: 'First grade')
        string(name: 'GRADE2', defaultValue: '90', description: 'Second grade')
    }

    stages {
        stage('Show Inputs') {
            steps {
                echo "Student: ${params.STUDENT_NAME}"
                echo "Grade 1: ${params.GRADE1}"
                echo "Grade 2: ${params.GRADE2}"
            }
        }

        stage('Calculate Average') {
            steps {
                script {
                    def avg = (params.GRADE1.toInteger() + params.GRADE2.toInteger()) / 2
                    echo "Average grade: ${avg}"

                    if (avg >= 60) {
                        echo "✅ PASSED"
                    } else {
                        error "❌ FAILED"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}
