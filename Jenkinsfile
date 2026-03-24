pipeline {
    agent any

    stage('Checkout') {
    steps {
        git branch: 'main', url: 'https://github.com/swethagandham2003/UI_AND_API_AUTOMATION.git'
    }
}

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
