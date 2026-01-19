pipeline {
    // בחירת ה-Node עליו ירוץ ה-Pipeline לפי בחירת המשתמש
    agent {
        label "${params.OPERATING_SYSTEM ?: 'built-in'}"
    }

    parameters {
        choice(name: 'OPERATING_SYSTEM', 
               choices: ['linux-node', 'built-in'], 
               description: 'בחר את השרת עליו תרצה להריץ את הבנייה')
               
        string(name: 'STUDENT_NAME', defaultValue: 'David', description: 'שם הסטודנט')
        string(name: 'GRADE1', defaultValue: '0', description: 'ציון ראשון')
        string(name: 'GRADE2', defaultValue: '0', description: 'ציון שני')
    }

    options {
        skipDefaultCheckout()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate & Calculate') {
            steps {
                script {
                    // יצירת תיקיית דוחות בצורה בטוחה
                    def reportsDir = "reports"
                    dir(reportsDir) { }

                    def errors = []
                    
                    def validateGrade = { gradeStr, name ->
                        try {
                            def g = gradeStr.toInteger()
                            if (g < 0 || g > 100) {
                                errors << "${name} מחוץ לטווח (0-100)"
                                return null
                            }
                            return g
                        } catch (e) {
                            errors << "${name} אינו מספר חוקי"
                            return null
                        }
                    }

                    def g1 = validateGrade(params.GRADE1, "ציון 1")
                    def g2 = validateGrade(params.GRADE2, "ציון 2")

                    def average = (g1 != null && g2 != null) ? (g1 + g2) / 2 : null
                    
                    // עיצוב ה-HTML החדש
                    def htmlContent = """
                    <!DOCTYPE html>
                    <html dir="rtl" lang="he">
                    <head>
                        <meta charset="UTF-8">
                        <style>
                            :root {
                                --primary: #4a90e2;
                                --success: #2ecc71;
                                --danger: #e74c3c;
                                --text: #2c3e50;
                                --bg: #f8f9fa;
                            }
                            body { 
                                font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; 
                                background-color: var(--bg); 
                                display: flex; 
                                justify-content: center; 
                                align-items: center; 
                                min-height: 100vh; 
                                margin: 0; 
                            }
                            .card { 
                                background: white; 
                                border-radius: 20px; 
                                box-shadow: 0 15px 35px rgba(0,0,0,0.1); 
                                width: 90%; 
                                max-width: 450px; 
                                padding: 40px; 
                                text-align: center; 
                            }
                            h1 { color: var(--text); font-size: 24px; margin-bottom: 30px; }
                            .student-name { color: var(--primary); font-weight: bold; }
                            
                            .stats-container { 
                                display: flex; 
                                justify-content: space-around; 
                                margin-bottom: 30px; 
                                background: #fdfdfd; 
                                border-radius: 15px; 
                                padding: 20px; 
                                border: 1px solid #eee;
                            }
                            .stat-box { display: flex; flex-direction: column; }
                            .stat-label { font-size: 14px; color: #7f8c8d; margin-bottom: 5px; }
                            .stat-value { font-size: 20px; font-weight: bold; color: var(--text); }
                            
                            .average-display { margin-bottom: 30px; }
                            .avg-label { font-size: 16px; color: #7f8c8d; }
                            .avg-value { font-size: 64px; font-weight: 800; color: var(--text); line-height: 1; }
                            
                            .status-badge { 
                                display: inline-block; 
                                padding: 12px 30px; 
                                border-radius: 50px; 
                                font-weight: bold; 
                                font-size: 18px; 
                                text-transform: uppercase; 
                            }
                            .passed { background-color: #d4edda; color: var(--success); }
                            .failed { background-color: #f8d7da; color: var(--danger); }
                            
                            .errors { color: var(--danger); margin-top: 20px; font-size: 14px; border-top: 1px dashed #ddd; padding-top: 10px; }
                            .footer { margin-top: 30px; font-size: 12px; color: #bdc3c7; }
                        </style>
                    </head>
                    <body>
                        <div class="card">
                            <h1>דוח ציונים עבור <span class="student-name">${params.STUDENT_NAME}</span></h1>
                            
                            <div class="stats-container">
                                <div class="stat-box">
                                    <span class="stat-label">ציון א'</span>
                                    <span class="stat-value">${g1 != null ? g1 : '-'}</span>
                                </div>
                                <div class="stat-box">
                                    <span class="stat-label">ציון ב'</span>
                                    <span class="stat-value">${g2 != null ? g2 : '-'}</span>
                                </div>
                            </div>

                            <div class="average-display">
                                <span class="avg-label">ממוצע סופי</span>
                                <div class="avg-value">${average != null ? average : '-'}</div>
                            </div>

                            ${errors ? """
                                <div class="errors">
                                    <strong>שגיאות שנמצאו:</strong><br>
                                    ${errors.join('<br>')}
                                </div>
                            """ : """
                                <div class="status-badge ${average >= 50 ? 'passed' : 'failed'}">
                                    ${average >= 50 ? 'עבר ✅' : 'נכשל ❌'}
                                </div>
                            """}

                            <div class="footer">
                                הופק על ידי Jenkins Pipeline<br>
                                שרת מבצע: ${env.NODE_NAME}
                            </div>
                        </div>
                    </body>
                    </html>
                    """
                    
                    writeFile file: "${reportsDir}/GradeReport.html", text: htmlContent
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
