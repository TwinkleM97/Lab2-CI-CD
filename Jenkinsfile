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
                bat 'C:\\Users\\twink\\AppData\\Local\\Programs\\Python\\Python311\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Flask application...'
                bat 'C:\\Users\\twink\\AppData\\Local\\Programs\\Python\\Python311\\python.exe -c "import flask; print(\'Flask OK\')"'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'C:\\Users\\twink\\AppData\\Local\\Programs\\Python\\Python311\\python.exe -m pytest test_app.py'
            }
        }

        stage('Notify') {
            steps {
                echo 'Build completed successfully!'
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
