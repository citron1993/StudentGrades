# StudentGrades
פרויקט גמר jenkins
# פרויקט ציוני תלמידים

## תיאור
פרויקט זה מחשב ציונים לתלמידים ומייצר דוח HTML וקובץ לוג.  
הפרויקט מותאם להרצה גם ב‑**Windows** וגם ב‑**Linux (WSL)**, ומשולב ב‑**Jenkins** לצורך ריצה אוטומטית בצינור CI/CD.  
**כל הפרויקט נעשה בעזרת ChatGPT.**

---

## קבצים בפרויקט
- `grades_calculator.py` – סקריפט Python שמחשב ציונים ומייצר דוחות.
- `Jenkinsfile` – קובץ קונפיגורציה לצינור Jenkins.
- `result.html` – דוח HTML שנוצר לאחר הרצת הסקריפט.
- `script.log` – קובץ לוג עם פרטי ביצוע הריצה.
- `README.md` – קובץ זה עם הסבר והוראות שימוש.

---

## דרישות
- Python 3.x מותקן על ה‑node (Windows או WSL בלינוקס)
- Jenkins עם גישה לרפוזיטורי ב‑GitHub
- Git מותקן על ה‑node

---

## איך להריץ

### 1. הרצה ידנית (Windows או Linux)
נווט לתיקיית הפרויקט והרץ:

```bash
# ב‑Windows
python grades_calculator.py <STUDENT_NAME> <GRADE1> <GRADE2> <PASSED_EXAM> <EXAM_DATE>

# בלינוקס / WSL
python3 grades_calculator.py <STUDENT_NAME> <GRADE1> <GRADE2> <PASSED_EXAM> <EXAM_DATE>
