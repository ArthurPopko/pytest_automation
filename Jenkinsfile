pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                branches: [[name: '*/master']],
                extensions: [],
                userRemoteConfigs: [[credentialsId: 'cdd4f772-d4c3-473c-9b2a-1056b608a551',
                url: 'git@github.com:ArthurPopko/pytest_automation.git']]])
            }
        }
        stage('ui qa run') {
                steps {
                    git credentialsId: 'cdd4f772-d4c3-473c-9b2a-1056b608a551', url: 'git@github.com:ArthurPopko/pytest_automation.git'
                    sh '''python3 -m venv ~/venvs/python310
                    source ~/venvs/python310/bin/activate
                    pip install -r requirements.txt
                    pytest -v -m qa --env qa --alluredir allure-results --parallel\''''
                }
        }
        stage('allure') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
       }
    }
}