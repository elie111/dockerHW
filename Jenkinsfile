pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
	}
	    stages {
        stage('Clone') {
            steps {
                    git branch: "main",url:'https://github.com/elie111/dockerHW.git'
            }
        }
	
	
		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW |  docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		
		stage('Build image') {

			steps {
				sh 'docker build -t eliehadd/dockerhw:latest .'
			}
		}


		stage('Push image') {

			steps {
				sh ' docker push eliehadd/dockerhw'
			}
		}
stage('Slack Notifications') {
            steps{
                slackSend baseUrl: 'https://hooks.slack.com/services/',
                channel: '#fursa-hw3',
                color: 'good',
                message: 'Image has been built and pushed to dockerhub',
                teamDomain: 'fursaHW',
                tokenCredentialId: 'slack-hw'
            }
        }
	}

	post {
		always {
			sh ' docker logout'
		}
	}

}
