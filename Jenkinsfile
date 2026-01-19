pipeline {
    agent any

    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'Student name')
        string(name: 'GRADE1', defaultValue: '80', description: 'Grade 1')
        string(name: 'GRADE2', defaultValue: '90', description: 'Grade 2')
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
                    int g1 = params.GRADE1.toInteger()
                    int g2 = params.GRADE2.toInteger()
                    float avg = (g1 + g2) / 2.0

                    echo "Average grade: ${avg}"

                    if (avg >= 60) {
                        echo "✅ PASSED"
                    } else {
                        echo "❌ FAILED"
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
