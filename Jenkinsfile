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
                bat 'python -m pip install flask'
                bat 'python -m pip install pytest'
            }
        }

        stage('Build') {
            steps {
                bat 'python -c "import flask; print(\'Flask OK\')"'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m py_compile app.py'
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
        failure {
            echo ' Pipeline failed!'
        }
    }
}
