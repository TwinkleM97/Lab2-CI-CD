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
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Simulating build step...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running basic tests...'
                bat 'echo No unit tests implemented yet.'
            }
        }

        stage('Notify') {
            steps {
                echo 'Build completed! Notification sent.'
            }
        }
    }
}
