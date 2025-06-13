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
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask application...'
                bat 'venv\\Scripts\\python.exe -c "import flask; print(\'Flask OK\')"'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat 'venv\\Scripts\\python.exe -m pytest test_app.py'
            }
        }

        stage('Notify') {
            steps {
                echo 'Build and test completed!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
