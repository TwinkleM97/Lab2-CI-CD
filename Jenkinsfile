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
                // Use PowerShell instead of batch
                powershell 'python -m pip install flask pytest'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building Flask application...'
                powershell 'python -c "import flask; print(\'Flask imported successfully\')"'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                powershell 'python -m py_compile app.py'
                powershell 'python -c "from app import app; print(\'App imported successfully\')"'
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
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}