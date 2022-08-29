pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                branches: [[name: '*/master']],
                extensions: [],
                userRemoteConfigs: [
                [refspec: '~/.ssh/id_rsa', url: 'git@github.com:ArthurPopko/pytest_automation.git']]
                ])
            }
        }


        stage('ui qa run') {
            parallel {
                stage('RUN TESTS IN PARALLEL A') {
                    steps {
                        source ~/venvs/python310/bin/activate
                        pip install -r requirements.txt
                        pytest -v -m qa --env qa --alluredir allure-results --parallel'
                    }
               }
            }
        }
    }
}
