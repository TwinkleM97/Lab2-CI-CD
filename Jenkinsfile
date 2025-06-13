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
                bat 'pip install flask'
                bat 'pip install pytest'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building Flask application...'
                bat 'python -c "import flask; print(\'Flask imported successfully\')"'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'python -m py_compile app.py'
                bat 'python -c "from app import app; print(\'App imported successfully\')"'
                echo 'Basic tests passed!'
            }
        }
        
        stage('Notify') {
            steps {
                echo 'Build completed successfully!'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}