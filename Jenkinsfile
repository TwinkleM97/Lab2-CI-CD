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
        bat '"C:\\Users\\twink\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install flask'
        bat '"C:\\Users\\twink\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install pytest'
    }
}

stage('Build') {
    steps {
        bat '"C:\\Users\\twink\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -c "import flask; print(\'Flask OK\')"'
    }
}

stage('Test') {
    steps {
        bat '"C:\\Users\\twink\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m py_compile app.py'
    }
}

        stage('Notify') {
            steps {
                echo '🎉 Pipeline completed successfully!'
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed. Please check logs.'
        }
    }
}
