pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/TwinkleM97/Lab2-CI-CD.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip.exe install --upgrade pip'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                bat 'venv\\Scripts\\python.exe -c "import flask; print(\'Flask OK\')"'
            }
        }

        stage('Test') {
            steps {
                bat 'venv\\Scripts\\python.exe -m py_compile app.py'
            }
        }

        stage('Notify') {
            steps {
                echo '✅ CI/CD pipeline completed!'
            }
        }
    }

    post {
        always {
            echo '🔁 Pipeline finished'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}
