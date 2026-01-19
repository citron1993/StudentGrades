pipeline {
    agent {
        label "${params.OPERATING_SYSTEM ?: 'built-in'}"
    }

    parameters {
        choice(name: 'OPERATING_SYSTEM', 
               choices: ['linux-node', 'built-in'], 
               description: 'בחר שרת להרצה')
               
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'שם הסטודנט')
        string(name: 'GRADE1', defaultValue: '0', description: 'ציון 1')
        string(name: 'GRADE2', defaultValue: '0', description: 'ציון 2')
    }

    stages {
        stage('Cleanup & Setup') {
            steps {
                script {
                    // יצירת תיקייה וניקוי קבצים ישנים כדי להבטיח עדכון
                    if (isUnix()) {
                        sh "mkdir -p reports && rm -f reports/*.html"
                    } else {
                        bat "if not exist reports mkdir reports"
                        bat "del /q reports\\*.html >nul 2>&1 || exit /b 0"
                    }
                }
            }
        }

        stage('Generate Modern Report') {
            steps {
                script {
                    def g1 = params.GRADE1.toInteger()
                    def g2 = params.GRADE2.toInteger()
                    def average = (g1 + g2) / 2
                    def status = (average >= 50) ? "עבר ✅" : "נכשל ❌"
                    def nodeName = env.NODE_NAME ?: "Built-in"

                    // עיצוב ה-HTML המודרני
                    def htmlContent = """
                    <!DOCTYPE html>
                    <html dir="rtl" lang="he">
                    <head>
                        <meta charset="UTF-8">
                        <style>
                            body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
                            .card { background: white; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); width: 400px; padding: 30px; text-align: center; }
                            h1 { color: #1a73e8; margin-bottom: 10px; }
                            .student { font-size: 1.2em; color: #5f6368; margin-bottom: 25px; }
                            .stats { display: flex; justify-content: space-around; background: #f8f9fa; padding: 15px; border-radius: 12px; margin-bottom: 20px; }
                            .stat-box { display: flex; flex-direction: column; }
                            .label { font-size: 0.8em; color: #70757a; }
                            .val { font-size: 1.2em; font-weight: bold; }
                            .avg-circle { margin: 20px auto; width: 120px; height: 120px; border-radius: 50%; border: 8px solid ${average >= 50 ? '#34a853' : '#ea4335'}; display: flex; flex-direction: column; justify-content: center; }
                            .avg-num { font-size: 2.5em; font-weight: 800; color: #3c4043; }
                            .status { font-size: 1.5em; font-weight: bold; margin-top: 15px; color: ${average >= 50 ? '#34a853' : '#ea4335'}; }
                            .footer { font-size: 0.7em; color: #bdc3c7; margin-top: 25px; border-top: 1px solid #eee; padding-top: 10px; }
                        </style>
                    </head>
                    <body>
                        <div class="card">
                            <h1>דוח ציונים</h1>
                            <div class="student">סטודנט: <strong>${params.STUDENT_NAME}</strong></div>
                            <div class="stats">
                                <div class="stat-box"><span class="label">ציון א'</span><span class="val">${g1}</span></div>
                                <div class="stat-box"><span class="label">ציון ב'</span><span class="val">${g2}</span></div>
                            </div>
                            <div class="avg-circle">
                                <span class="label">ממוצע</span>
                                <span class="avg-num">${average}</span>
                            </div>
                            <div class="status">${status}</div>
                            <div class="footer">הופק ע"י Jenkins | שרת: ${nodeName} | ${new Date().format('dd/MM/yyyy HH:mm')}</div>
                        </div>
                    </body>
                    </html>
                    """
                    writeFile file: "reports/GradeReport.html", text: htmlContent

                    // לוג טקסטואלי נקי שמתעדכן תמיד
                    def logContent = "Build Log for ${params.STUDENT_NAME}\n" +
                                     "Timestamp: ${new Date().toString()}\n" +
                                     "Grades: ${g1}, ${g2} | Average: ${average}\n" +
                                     "Result: ${status}\n" +
                                     "Node: ${nodeName}"
                    writeFile file: "reports/BuildLog.html", text: logContent
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}
