pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Spécifier explicitement la branche main
                git branch: 'main', url: 'https://github.com/AybTGH/app-jenkins.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                sh 'docker build -t myapp:latest .'
            }
        }
        stage('Deploy') {
            steps {
                // Arrêter le container si existant
                sh 'docker stop myapp || true'
                sh 'docker rm myapp || true'
                // Run container
                sh 'docker run -d -p 5000:5000 --name myapp myapp:latest'
            }
        }
    }
}

