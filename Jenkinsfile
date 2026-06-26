// Jenkinsfile -- Jenkins' equivalent of GitHub Actions' ci.yml
// This defines the pipeline stages Jenkins will run.

pipeline {
    agent any   // run on any available Jenkins agent/machine

    stages {

        stage('Checkout') {
            steps {
                // Jenkins already does this automatically when using
                // "Pipeline script from SCM", but it's good to see it explicitly.
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                sh 'pytest test_app.py -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t cicd-demo:latest .'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! ✅'
        }
        failure {
            echo 'Pipeline failed. Check the logs above. ❌'
        }
    }
}
