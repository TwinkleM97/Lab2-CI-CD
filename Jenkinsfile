pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/TwinkleM97/Lab2-CI-CD.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'setup.bat'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask app...'
                bat 'call venv\\Scripts\\activate.bat && python -c "import flask; print(\'Flask imported\')"'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'call venv\\Scripts\\activate.bat && python -m py_compile app.py'
                bat 'call venv\\Scripts\\activate.bat && python -c "from app import app; print(\'App imported\')"'
            }
        }

        stage('Notify') {
            steps {
                echo 'All stages ran. Notification step done.'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline succeeded!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
