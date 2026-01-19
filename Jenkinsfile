Started by user itay citron
Obtained Jenkinsfile from git https://github.com/citron1993/StudentGrades.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in C:\ProgramData\Jenkins\.jenkins\workspace\Grades-Pipeline-Git
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git.exe rev-parse --resolve-git-dir C:\ProgramData\Jenkins\.jenkins\workspace\Grades-Pipeline-Git\.git # timeout=10
Fetching changes from the remote Git repository
 > git.exe config remote.origin.url https://github.com/citron1993/StudentGrades.git # timeout=10
Fetching upstream changes from https://github.com/citron1993/StudentGrades.git
 > git.exe --version # timeout=10
 > git --version # 'git version 2.49.0.windows.1'
 > git.exe fetch --tags --force --progress -- https://github.com/citron1993/StudentGrades.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git.exe rev-parse "refs/remotes/origin/main^{commit}" # timeout=10
Checking out Revision 1c2dd06fbb142ee0da32e048b703f226bb378ec2 (refs/remotes/origin/main)
 > git.exe config core.sparsecheckout # timeout=10
 > git.exe checkout -f 1c2dd06fbb142ee0da32e048b703f226bb378ec2 # timeout=10
Commit message: "Jenkinsfile"
 > git.exe rev-list --no-walk 1c2dd06fbb142ee0da32e048b703f226bb378ec2 # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Show Inputs)
[Pipeline] echo
Student: David
[Pipeline] echo
Grade 1: 50
[Pipeline] echo
Grade 2: 40
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Calculate Average)
[Pipeline] script
[Pipeline] {
[Pipeline] echo
Average grade: 45
[Pipeline] error
[Pipeline] }
[Pipeline] // script
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] echo
Pipeline finished
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
ERROR: ❌ FAILED
Finished: FAILURE
