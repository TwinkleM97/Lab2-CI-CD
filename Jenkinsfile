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
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
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
                sh 'echo "No unit tests implemented yet."'
            }
        }

        stage('Notify') {
            steps {
                echo 'Build completed! Notification sent.'
            }
        }
    }
}
