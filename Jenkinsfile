pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/TwinkleM97/Lab2-CI-CD.git'
            }
        }

        stage('Setup Virtual Env') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                python -m ensurepip --upgrade
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                python -c "import flask; print('Flask OK')"
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                pytest test_app.py
                '''
            }
        }

        stage('Notify') {
            steps {
                echo 'All stages completed!'
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
