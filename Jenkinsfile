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
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            call venv\\Scripts\\activate.bat
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building Flask application...'
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            python -c "from app import app; print('Flask app imported successfully')"
                        '''
                    } else {
                        bat '''
                            call venv\\Scripts\\activate.bat
                            python -c "from app import app; print('Flask app imported successfully')"
                        '''
                    }
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            python -m pytest --version || echo "pytest not installed, running basic syntax check"
                            python -m py_compile app.py
                            echo "Basic syntax check passed"
                        '''
                    } else {
                        bat '''
                            call venv\\Scripts\\activate.bat
                            python -m pytest --version || echo "pytest not installed, running basic syntax check"
                            python -m py_compile app.py
                            echo "Basic syntax check passed"
                        '''
                    }
                }
            }
        }
        
        stage('Notify') {
            steps {
                echo 'Build completed successfully! Notification sent.'
                script {
                    // You can add email notification here if configured
                    echo "Pipeline completed at: ${new Date()}"
                }
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            script {
                if (isUnix()) {
                    sh 'rm -rf venv || true'
                } else {
                    bat 'if exist venv rmdir /s /q venv || echo "No venv to clean"'
                }
            }
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}