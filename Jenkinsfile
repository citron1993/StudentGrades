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
                // מוריד את הקוד מה-Git
                checkout scm
            }
        }

        stage('Validate & Calculate') {
            steps {
                script {
                    // יצירת תיקיית דוחות בצורה בטוחה (Cross-Platform)
                    def reportsDir = "reports"
                    dir(reportsDir) { }

                    def errors = []
                    
                    // פונקציה לבדיקת תקינות ציונים
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
                    def status = (average != null && average >= 50) ? "PASSED" : "FAILED"

                    // יצירת ה-HTML עם העיצוב המודרני
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
                                --bg: #f4f7f6;
                            }
                            body { font-family: 'Segoe UI', Arial, sans-serif; background: var(--bg); display: flex; justify-content: center; padding-top: 50px; }
                            .card { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); width: 100%; max-width: 500px; }
                            h1 { text-align: center; color: #333; margin-bottom: 30px; border-bottom: 3px solid var(--primary); padding-bottom: 10px; }
                            .stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px; }
                            .stat-item { background: #f9f9f9; padding: 15px; border-radius: 10px; text-align: center; }
                            .label { display: block; color: #888; font-size: 0.9em; margin-bottom: 5px; }
                            .value { font-size: 1.4em; font-weight: bold; color: #333; }
                            .result-box { text-align: center; padding: 20px; border-radius: 10px; margin-top: 20px; }
                            .passed { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
                            .failed { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
                            .error-text { color: var(--danger); font-size: 0.9em; text-align: center; }
                        </style>
                    </head>
                    <body>
                        <div class="card">
                            <h1>דוח ציונים: ${params.STUDENT_NAME}</h1>
                            <div class="stat-grid">
                                <div class="stat-item"><span class="label">ציון א'</span><span class="value">${g1 != null ? g1 : '-'}</span></div>
                                <div class="stat-item"><span class="label">ציון ב'</span><span class="value">${g2 != null ? g2 : '-'}</span></div>
                            </div>
                            <div style="text-align:center;">
                                <span class="label">ממוצע סופי</span>
                                <div class="value" style="font-size: 3em;">${average != null ? average : '-'}</div>
                            </div>
                            
                            <div class="result-box ${average != null && average >= 50 ? 'passed' : 'failed'}">
                                <h2 style="margin:0;">${errors ? 'שגיאה בנתונים' : (average >= 50 ? 'עבר ✅' : 'נכשל ❌')}</h2>
                            </div>
                            
                            ${errors ? "<div class='error-text'><p>שגיאות: ${errors.join(', ')}</p></div>" : ""}
                            
                            <p style="text-align:center; color:#bbb; font-size:0.8em; margin-top:20px;">הופק על ידי Jenkins | Node: ${env.NODE_NAME}</p>
                        </div>
                    </body>
                    </html>
                    """
                    
                    // כתיבת הקובץ
                    writeFile file: "${reportsDir}/GradeReport.html", text: htmlContent
                    
                    echo "The report has been generated successfully."
                }
            }
        }
    }

    post {
        always {
            // שמירת הקובץ כארטיפקט בתוך ג'נקינס
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}
