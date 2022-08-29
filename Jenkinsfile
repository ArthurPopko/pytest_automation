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
                    sh '''sh create_testplan.sh
                    python3 -m venv ~/venvs/python310
                    source ~/venvs/python310/bin/activate
                    pip install -r requirements.txt
                    pytest -v -m qa --env qa --testrail --tr-config=testrail-ui.cfg --alluredir allure-results'''
                }
        }
        stage('api dev run') {
                steps {
                    git credentialsId: 'cdd4f772-d4c3-473c-9b2a-1056b608a551', url: 'git@github.com:ArthurPopko/pytest_automation.git'
                    sh '''python3 -m venv ~/venvs/python310
                    source ~/venvs/python310/bin/activate
                    pip install -r requirements.txt
                    pytest -v -m api --env dev --testrail --tr-config=testrail-api.cfg --alluredir allure-results'''
                }
        }
        stage('data parallel run') {
                steps {
                    git credentialsId: 'cdd4f772-d4c3-473c-9b2a-1056b608a551', url: 'git@github.com:ArthurPopko/pytest_automation.git'
                    sh '''python3 -m venv ~/venvs/python310
                    source ~/venvs/python310/bin/activate
                    pip install -r requirements.txt
                    pytest -v -m data -n 4 --env dev --alluredir allure-results'''
                }
        }
        stage('ui dev run') {
                steps {
                    git credentialsId: 'cdd4f772-d4c3-473c-9b2a-1056b608a551', url: 'git@github.com:ArthurPopko/pytest_automation.git'
                    sh '''sh create_testplan.sh
                    python3 -m venv ~/venvs/python310
                    source ~/venvs/python310/bin/activate
                    pip install -r requirements.txt
                    pytest -v -m 'dev and ui' --env dev --testrail --tr-config=testrail-ui.cfg --alluredir allure-results'''
                }
        }
        stage('allure') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
       }
    }
}