pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/AybTGH/app-jenkins.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp:latest .'
            }
        }
        stage('Deploy') {
            steps {
                // Arrêter le container si existant
                sh 'docker stop myapp || true'
                sh 'docker rm myapp || true'
                // Run container
                sh 'docker run -d -p 5000:5000 --name flask-viz-app flask-viz-app:latest'
            }
        }
    }
}
