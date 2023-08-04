pipeline {
    agent any
    stages {
        stage('1 - Initialising') {
            steps {
                echo 'Initialising cleanup'
                sh 'docker rm -f $(docker ps -aq) || true'
            }
        }
        stage('B - Build') {
            steps {
                echo 'Building project'
            sh 'docker build -t obtas/chatbot2 .'
            }
        }
        stage('2 - Test') {
            steps {
                sh 'python --version'
            }
        }
        stage('3 - Deploy') {
            steps {
                sh 'docker run -d -p 80:80 obtas/chatbot2'
            }
        }
    }
}